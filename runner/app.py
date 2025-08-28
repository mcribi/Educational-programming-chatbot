from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
import subprocess, tempfile, os, re

# Shared temp base between host and runner (bind-mounted /tmp)
TMP_BASE = os.environ.get("RUNNER_TMP", "/tmp")

api = FastAPI(title="cpp-runner", version="1.1")

# Minimal security filters
BANNED_HEADERS = [
    r"<filesystem>", r"<fstream>", r"<cstdio>", r"<stdio\.h>",
    r"<dirent\.h>", r"<sys/.*>", r"<unistd\.h>", r"<dlfcn\.h>", r"<windows\.h>"
]
BANNED_FUNCS = [
    r"\bsystem\s*\(", r"\bfork\s*\(", r"\bexecl?\w*\s*\(", r"\bpopen\s*\(",
    r"\bfopen\s*\(", r"\bfreopen\s*\(", r"\bremove\s*\(", r"\brename\s*\("
]

# Limits and resources
MAX_CODE_BYTES   = 20_000  # 20 KB
COMPILE_TIMEOUT  = int(os.getenv("COMPILE_TIMEOUT", "25"))
RUN_TIMEOUT      = int(os.getenv("RUN_TIMEOUT", "2"))

COMPILE_CPUS     = os.getenv("COMPILE_CPUS", "1.0")
RUN_CPUS         = os.getenv("RUN_CPUS", "0.5")

COMPILE_MEMORY   = os.getenv("COMPILE_MEMORY", "256m")
RUN_MEMORY       = os.getenv("RUN_MEMORY", "128m")
PIDS             = "64"

# ---------- Request models ----------
class RunRequest(BaseModel):
    code: str = Field(..., description="C++ source in a code block or raw")

class RunTest(BaseModel):
    input: str = ""
    output: str = ""

class RunTestsRequest(BaseModel):
    code: str
    tests: List[RunTest]
    time_limit_ms: int = 1500
    memory_limit_mb: int = 128
    checker: str = "normalized"   # "exact" | "normalized" | "float"
    float_tol: Optional[float] = None

# ---------- Helpers ----------
def extract_cpp(code: str) -> str:
    """Accepts ```cpp ...``` blocks or returns the raw code."""
    m = re.search(r"```(?:cpp|c\+\+|cc)?\s*(.*?)```", code, re.DOTALL | re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return code.strip()

def looks_malicious(src: str) -> Optional[str]:
    """Very small allow/block list, just to avoid obvious escapes."""
    for pat in BANNED_HEADERS:
        if re.search(pat, src):
            return f"Uso de cabecera bloqueada: {pat}"
    for pat in BANNED_FUNCS:
        if re.search(pat, src):
            return f"Uso de llamada bloqueada: {pat}"
    return None

def _normalize(s: str) -> str:
    """Collapse runs of whitespace within each line, keep trailing newline if any."""
    lines = [(" ".join(line.rstrip().split())) for line in s.splitlines()]
    return ("\n".join(lines).rstrip() + ("\n" if s.endswith("\n") else "")) if s else s

def _compare(out: str, exp: str, checker: str, tol: Optional[float]):
    """Compare outputs according to checker strategy."""
    if checker == "exact":
        ok = (out == exp)
        diff = None if ok else f"Esperado:\n{exp}\nObtenido:\n{out}"
        return ok, diff
    elif checker == "float":
        def toks(x): return [t for t in x.strip().split()]
        ao, ae = toks(out), toks(exp)
        if len(ao) != len(ae):
            return False, f"Tokens distintos: esperado {len(ae)}, obtenido {len(ao)}"
        tol = tol or 1e-6
        for i, (x, y) in enumerate(zip(ao, ae)):
            try:
                if abs(float(x) - float(y)) > tol:
                    return False, f"Token {i}: esperado {y}, obtenido {x} (tol={tol})"
            except ValueError:
                if x != y:
                    return False, f"Token {i}: esperado {y}, obtenido {x}"
        return True, None
    else:  # normalized
        no, ne = _normalize(out), _normalize(exp)
        ok = (no == ne)
        diff = None if ok else f"Esperado(normalizado):\n{ne}\nObtenido(normalizado):\n{no}"
        return ok, diff

# ---------- /run (single run, no tests) ----------
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

    # Temporary folder on host (bind-mounted /tmp ensures sandbox sees it)
    tmpdir = tempfile.mkdtemp(prefix="cpp_", dir=TMP_BASE)
    src_path = os.path.join(tmpdir, "main.cpp")
    with open(src_path, "w") as f:
        f.write(src)

    image = "cpp-sandbox:latest"
    exe_ct = "/work/a.out"

    # Compile once to /work/a.out (persisted under mounted tmpdir)
    compile_cmd = [
        "docker", "run", "--rm",
        "--network=none",
        "--cpus", COMPILE_CPUS,
        "--memory", COMPILE_MEMORY,
        "--pids-limit", PIDS,
        "--read-only",
        "--cap-drop=ALL",
        "--security-opt", "no-new-privileges",
        "--tmpfs", "/tmp:rw,noexec,nosuid,nodev,size=16m",
        "-v", f"{tmpdir}:/work:rw",
        image,
        "bash", "-lc",
        f"g++ -std=c++17 -O2 -pipe -s -o {exe_ct} /work/main.cpp"
    ]

    try:
        c = subprocess.run(compile_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           text=True, timeout=COMPILE_TIMEOUT)
    except subprocess.TimeoutExpired:
        return {"ok": False, "stage": "compile", "stderr": "Timeout de compilación"}

    if c.returncode != 0:
        return {"ok": False, "stage": "compile", "stderr": c.stderr[:8000]}

    # Run with strict limits (same image, RO mount)
    time_secs = max(1, int(RUN_TIMEOUT))
    run_cmd = [
        "docker", "run", "--rm", "-i",
        "--network=none",
        "--cpus", RUN_CPUS,
        "--memory", RUN_MEMORY,
        "--pids-limit", PIDS,
        "--read-only",
        "--cap-drop=ALL",
        "--security-opt", "no-new-privileges",
        "--tmpfs", "/tmp:rw,noexec,nosuid,nodev,size=16m",
        "-v", f"{tmpdir}:/work:ro",
        image,
        "bash", "-lc",
        f"ulimit -t {time_secs} -v 262144 && {exe_ct}"
    ]
    try:
        r = subprocess.run(run_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           text=True, timeout=time_secs + 1)
    except subprocess.TimeoutExpired:
        return {"ok": False, "stage": "run", "stderr": "Timeout de ejecución"}

    return {"ok": True, "stdout": r.stdout[:8000], "stderr": r.stderr[:4000], "exit_code": r.returncode}

# ---------- /run_tests (compile once, run N tests) ----------
@api.post("/run_tests")
def run_tests(req: RunTestsRequest):
    src = extract_cpp(req.code)
    if not src:
        raise HTTPException(400, "Código vacío.")
    if len(src.encode("utf-8")) > MAX_CODE_BYTES:
        raise HTTPException(400, f"Código demasiado largo (> {MAX_CODE_BYTES} bytes).")

    bad = looks_malicious(src)
    if bad:
        return {"status": "blocked", "compile_log": bad, "cases": [], "passed": 0, "total": 0}

    # Prepare temp dir
    tmpdir = tempfile.mkdtemp(prefix="cpp_", dir=TMP_BASE)
    src_path = os.path.join(tmpdir, "main.cpp")
    with open(src_path, "w") as f:
        f.write(src)

    image = "cpp-sandbox:latest"
    exe_ct = "/work/a.out"
    time_secs = max(1, int(req.time_limit_ms / 1000))

    # Compile once
    compile_cmd = [
        "docker", "run", "--rm",
        "--network=none",
        "--cpus", COMPILE_CPUS,
        "--memory", COMPILE_MEMORY,
        "--pids-limit", PIDS,
        "--read-only",
        "--cap-drop=ALL",
        "--security-opt", "no-new-privileges",
        "--tmpfs", "/tmp:rw,noexec,nosuid,nodev,size=16m",
        "-v", f"{tmpdir}:/work:rw",
        image,
        "bash", "-lc",
        f"g++ -std=c++17 -O2 -pipe -s -o {exe_ct} /work/main.cpp"
    ]
    try:
        c = subprocess.run(compile_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           text=True, timeout=COMPILE_TIMEOUT)
    except subprocess.TimeoutExpired:
        return {
            "status": "CE", "compile_log": "Timeout de compilación",
            "cases": [], "passed": 0, "total": len(req.tests)
        }
    if c.returncode != 0:
        tail = "\n".join(c.stderr.splitlines()[-15:])
        return {
            "status": "CE", "compile_log": tail,
            "cases": [], "passed": 0, "total": len(req.tests)
        }

    # Run each test
    passed = 0
    cases = []
    overall = "AC"

    for i, t in enumerate(req.tests):
        run_cmd = [
            "docker", "run", "--rm", "-i",
            "--network=none",
            "--cpus", RUN_CPUS,
            "--memory", RUN_MEMORY,
            "--pids-limit", PIDS,
            "--read-only",
            "--cap-drop=ALL",
            "--security-opt", "no-new-privileges",
            "--tmpfs", "/tmp:rw,noexec,nosuid,nodev,size=16m",
            "-v", f"{tmpdir}:/work:ro",
            image,
            "bash", "-lc",
            f"ulimit -t {time_secs} -v 262144 && {exe_ct}"
        ]
        try:
            rr = subprocess.run(
                run_cmd,
                input=t.input,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                text=True,
                timeout=time_secs + 1
            )
        except subprocess.TimeoutExpired:
            cases.append({"i": i, "status": "TLE"})
            if overall == "AC":
                overall = "TLE"
            continue

        if rr.returncode != 0:
            tail = "\n".join(rr.stderr.splitlines()[-10:])
            cases.append({"i": i, "status": "RE", "stderr": tail})
            if overall == "AC":
                overall = "RE"
            continue

        ok, diff = _compare(rr.stdout, t.output, req.checker, req.float_tol)
        if ok:
            cases.append({"i": i, "status": "AC"})
            passed += 1
        else:
            cases.append({"i": i, "status": "WA", "diff": (diff or "")[:1000]})
            if overall == "AC":
                overall = "WA"

    return {
        "status": "AC" if passed == len(req.tests) else overall,
        "compile_log": "",
        "cases": cases,
        "passed": passed,
        "total": len(req.tests),
    }
