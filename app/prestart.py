import subprocess
import sys

from alembic.config import Config
from alembic import command

from app.main import ROOT


if __name__ == "__main__":
    alembic_cfg = Config(ROOT / "alembic.ini")

    subprocess.run([sys.executable, "./backend_pre_start.py"])
    # command.upgrade(alembic_cfg, "head")
    subprocess.run([sys.executable, "./initial_data.py"])
