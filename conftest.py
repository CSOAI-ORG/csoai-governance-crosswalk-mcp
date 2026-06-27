"""conftest for csoai-governance-crosswalk-mcp.

Resets BOTH the in-process rate limiter (`server._usage`) AND the
on-disk usage ledger (`~/.meok/usage.json`) before each test so the
free-tier daily cap doesn't poison test runs.

In CI each test process is fresh, so this is purely for local-dev
convenience and zero risk in production.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


def pytest_configure(config):
    """Pre-import server + auth_middleware so we can poke at their state."""
    try:
        import server  # noqa: F401
        import auth_middleware  # noqa: F401
        config._csoai_server = server
        config._csoai_auth = auth_middleware
    except Exception:
        config._csoai_server = None
        config._csoai_auth = None


def _reset_rate_limiters():
    """Clear both the in-memory and on-disk rate-limiter state."""
    try:
        import server
        if hasattr(server, "_usage"):
            server._usage.clear()
    except Exception:
        pass
    try:
        import auth_middleware
        uf = getattr(auth_middleware, "USAGE_FILE", None)
        if uf and os.path.exists(uf):
            # Save a backup once, then reset to {}
            backup = uf + ".test-backup"
            if not os.path.exists(backup):
                import shutil
                shutil.copy2(uf, backup)
            with open(uf, "w") as f:
                json.dump({}, f)
    except Exception:
        pass


def pytest_runtest_setup(item):
    _reset_rate_limiters()


def pytest_runtest_teardown(item, nextitem):
    _reset_rate_limiters()