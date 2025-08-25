from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import subprocess, tempfile, os, textwrap, re, json, uuid

api = FastAPI(title="cpp-runner", version="1.0")

#small whitelist/blocking of dangerous includes and functions
BANNED_HEADERS = [
    r"<filesystem>", r"<fstream>", r"<cstdio>", r"<stdio\.h>",
    r"<dirent\.h>", r"<sys/.*>", r"<unistd\.h>", r"<dlfcn\.h>", r"<windows\.h>"
]
BANNED_FUNCS = [r"\bsystem\s*\(", r"\bfork\s*\(", r"\bexecl?\w*\s*\(", r"\bpopen\s*\(",
                r"\bfopen\s*\(", r"\bfreopen\s*\(", r"\bremove\s*\(", r"\brename\s*\("]

MAX_CODE_BYTES = 20_000  # 20 KB
COMPILE_TIMEOUT = 5       # seconds
RUN_TIMEOUT = 2           # seconds
# resource limits for the execution container:
MEMORY = "128m"
CPUS = "0.5"
PIDS = "64"

class RunRequest(BaseModel):
    code: str = Field(..., description="C++ source in a code block or raw")

def extract_cpp(code: str) -> str:
    """
    Accepts blocks ```cpp ... ``` or returns as is if there are no triple backticks.
    """
    m = re.search(r"```(?:cpp|c\+\+|cc)?\s*(.*?)```", code, re.DOTALL | re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return code.strip()

def looks_malicious(src: str) -> str | None:
    for pat in BANNED_HEADERS:
        if re.search(pat, src):
            return f"Uso de cabecera bloqueada: {pat}"
    for pat in BANNED_FUNCS:
        if re.search(pat, src):
            return f"Uso de llamada bloqueada: {pat}"
    return None

@api.post("/run")
def run_code(req: RunRequest):
    src = extract_cpp(req.code)
    if not src:
        raise HTTPException(400, "Código vacío.")
    if len(src.encode("utf-8")) > MAX_CODE_BYTES:
        raise HTTPException(400, f"Código demasiado largo (> {MAX_CODE_BYTES} bytes).")

    bad = looks_malicious(src)
    if bad:
        return {"ok": False, "stage": "blocked", "stderr": bad}

    # Temporary file
    tmpdir = tempfile.mkdtemp(prefix="cpp_")
    src_path = os.path.join(tmpdir, "main.cpp")
    with open(src_path, "w") as f:
        f.write(src)

    image = "cpp-sandbox:latest"  # super-restricted ephemeral image (below)
    exe_name = "a.out"
    compile_cmd = [
        "docker", "run", "--rm",
        "--network=none",
        "--cpus", CPUS,
        "--memory", MEMORY,
        "--pids-limit", PIDS,
        "--read-only",
        "--cap-drop=ALL",
        "--security-opt", "no-new-privileges",
        "--tmpfs", "/tmp:rw,noexec,nosuid,nodev,size=16m",
        "-v", f"{src_path}:/work/main.cpp:ro",
        image,
        "bash", "-lc",
        f"g++ -std=c++17 -O2 -pipe -static -s -o /tmp/{exe_name} /work/main.cpp"
    ]

    try:
        c = subprocess.run(compile_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           text=True, timeout=COMPILE_TIMEOUT)
    except subprocess.TimeoutExpired:
        return {"ok": False, "stage": "compile", "stderr": "Timeout de compilación"}

    if c.returncode != 0:
        return {"ok": False, "stage": "compile", "stderr": c.stderr[:8000]}

    # Run binary with strict limits (same image, read-only FS, no network)
    run_cmd = [
        "docker", "run", "--rm",
        "--network=none",
        "--cpus", CPUS,
        "--memory", MEMORY,
        "--pids-limit", PIDS,
        "--read-only",
        "--cap-drop=ALL",
        "--security-opt", "no-new-privileges",
        "--tmpfs", "/tmp:rw,noexec,nosuid,nodev,size=16m",
        image,
        "bash", "-lc",
        f"ulimit -t {RUN_TIMEOUT} -v 262144 && /tmp/{exe_name}"
    ]
    try:
        r = subprocess.run(run_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           text=True, timeout=RUN_TIMEOUT+1)
    except subprocess.TimeoutExpired:
        return {"ok": False, "stage": "run", "stderr": "Timeout de ejecución"}

    return {"ok": True, "stdout": r.stdout[:8000], "stderr": r.stderr[:4000], "exit_code": r.returncode}
