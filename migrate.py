import importlib
import os
from pathlib import Path
import shutil
import subprocess  # nosec B404
import sys

def run_migrations():
    env = os.environ.copy()
    env.setdefault("FREENIT_ENV", "prod")
    oxyde = shutil.which("oxyde")
    if oxyde is None:
        candidate = Path(sys.executable).with_name("oxyde")
        if candidate.exists():
            oxyde = str(candidate)
        else:
            raise RuntimeError("oxyde executable not found in PATH")
    subprocess.run([oxyde, "migrate"], check=True, env=env)  # nosec B603


def db_setup():
    run_migrations()

    from name import app_name

    return importlib.import_module(f"{app_name}.app")


if __name__ == "__main__":
    db_setup()
