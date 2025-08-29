import httpx
import os
from config import RUNNER_URL

RUNNER_URL = os.getenv("RUNNER_URL", "http://runner:8000")

class RunnerError(Exception):
    pass

# async def run_cpp(*args, **kwargs):
#     raise RunnerError("run_cpp is deprecated; use /run and /submit (run_tests).")
async def run_cpp(code: str) -> dict:
    """Call runner /run endpoint (single compile & run, no tests)."""
    payload = {"code": code}
    timeout = httpx.Timeout(30.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            r = await client.post(f"{RUNNER_URL}/run", json=payload)
        except httpx.RequestError as e:
            raise RunnerError(str(e))
    if r.status_code >= 400:
        raise RunnerError(f"{r.status_code} {r.text}")
    return r.json()

async def run_tests(code: str, tests: list[dict], *, time_limit_ms=1500, memory_limit_mb=128, checker="normalized", float_tol=None):
    payload = {
        "code": code,
        "tests": tests,
        "time_limit_ms": time_limit_ms,
        "memory_limit_mb": memory_limit_mb,
        "checker": checker,
        "float_tol": float_tol,
    }
    async with httpx.AsyncClient(timeout=30.0) as client:
        r = await client.post(f"{RUNNER_URL}/run_tests", json=payload)
        r.raise_for_status()
        return r.json()
