#!/data/data/com.termux/files/usr/bin/bash

set -e

ROOT="$(git rev-parse --show-toplevel)"

mkdir -p "$ROOT/python/ados/cli"
mkdir -p "$ROOT/python/ados/config"

########################################
# config loader
########################################

cat > "$ROOT/python/ados/config/config.py" <<'PY'
from pathlib import Path
import yaml

CONFIG_DIR = Path.home() / ".ados"

def load_workspace():
    workspace = CONFIG_DIR / "workspace.yaml"

    if not workspace.exists():
        raise FileNotFoundError(workspace)

    with open(workspace,"r",encoding="utf-8") as f:
        return yaml.safe_load(f)
PY

########################################
# workspace service
########################################

cat > "$ROOT/python/ados/workspace/workspace.py" <<'PY'
from pathlib import Path
import subprocess

from ados.config.config import load_workspace

class Workspace:

    def scan(self):

        data = load_workspace()

        print("=" * 45)
        print(" ADOS Workspace Scan")
        print("=" * 45)

        print()

        print("Workspace :", data["workspace"]["name"])
        print("Owner     :", data["workspace"]["owner"])

        print()

        print("Repositories")

        repos = data.get("repositories", {})

        for name, repo in repos.items():

            path = Path(repo["path"])

            ok = path.exists()

            branch = "-"

            if ok and (path / ".git").exists():

                try:

                    branch = subprocess.check_output(
                        ["git","-C",str(path),
                         "branch","--show-current"],
                        text=True
                    ).strip()

                except Exception:
                    branch = "?"

            print()

            print(name)

            print("  Path   :", path)

            print("  Branch :", branch)

            print("  Status :", "OK" if ok else "NOT FOUND")
PY

########################################
# cli
########################################

cat > "$ROOT/python/ados/cli/workspace.py" <<'PY'
from ados.workspace.workspace import Workspace

def run(args):

    if not args:
        print("workspace commands:")
        print(" scan")
        return

    if args[0] == "scan":
        Workspace().scan()
        return

    print("Unknown workspace command")
PY

########################################
# main.py
########################################

cat > "$ROOT/python/ados/main.py" <<'PY'
#!/usr/bin/env python3

import sys

from ados.cli.workspace import run as workspace

def banner():
    print("=" * 45)
    print(" ADOS Python Runtime")
    print("=" * 45)

def main():

    banner()

    if len(sys.argv) < 2:
        print()
        print("Usage:")
        print(" workspace scan")
        return

    command = sys.argv[1]

    if command == "workspace":
        workspace(sys.argv[2:])
        return

    print("Unknown command:", command)

if __name__ == "__main__":
    main()
PY

chmod +x "$ROOT/python/ados/main.py"

########################################
# requirements
########################################

cat > "$ROOT/python/requirements.txt" <<'REQ'
PyYAML>=6.0
REQ

echo
echo "Workspace Scan Installed."
echo
