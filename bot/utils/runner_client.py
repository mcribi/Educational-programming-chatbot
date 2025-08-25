import httpx
from config import RUNNER_URL

class RunnerError(Exception):
    pass

async def run_cpp(code: str, stdin: str | None = None) -> dict:
    """
    Call the runner. Return a dict with:
    {
      "ok": bool,
      "stage": "compile"|"run",
      "stdout": "str",
      "stderr": "str",
      "time_ms": int,
      "exit_code": int | None
    }
    """
    payload = {
        "language": "cpp",
        "code": code,
        "stdin": stdin or "",
        #The limits are imposed by the runner: the user cannot change them.
        "time_limit_ms": 2000,
        "memory_limit_mb": 64,
    }
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            r = await client.post(f"{RUNNER_URL}/run", json=payload)
        except httpx.RequestError as e:
            raise RunnerError(f"No se pudo contactar con el runner: {e}") from e

    if r.status_code != 200:
        raise RunnerError(f"Runner devolvió {r.status_code}: {r.text}")

    data = r.json()
    # We normalise expected fields:
    return {
        "ok": bool(data.get("ok", False)),
        "stage": data.get("stage", "run"),
        "stdout": data.get("stdout", ""),
        "stderr": data.get("stderr", ""),
        "time_ms": int(data.get("time_ms") or 0),
        "exit_code": data.get("exit_code"),
    }
