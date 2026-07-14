#!/data/data/com.termux/files/usr/bin/bash
set -e

ROOT="$(git rev-parse --show-toplevel)"

mkdir -p "$ROOT/python/ados/router"

####################################################
# router.py
####################################################

cat > "$ROOT/python/ados/router/router.py" <<'PY'
from ados.cli.workspace import run as workspace
from ados.cli.state import run as state

COMMANDS = {
    "workspace": workspace,
    "state": state,
}

def dispatch(argv):

    if len(argv) < 2:
        print("")
        print("ADOS Commands")
        print("")
        for cmd in sorted(COMMANDS.keys()):
            print(" ", cmd)
        return

    command = argv[1]

    if command not in COMMANDS:
        print("Unknown command:", command)
        return

    COMMANDS[command](argv[2:])
PY

####################################################
# update main.py
####################################################

cat > "$ROOT/python/ados/main.py" <<'PY'
#!/usr/bin/env python3

import sys
from ados.router.router import dispatch

def banner():
    print("=" * 45)
    print(" ADOS Python Runtime")
    print("=" * 45)

def main():
    banner()
    dispatch(sys.argv)

if __name__ == "__main__":
    main()
PY

chmod +x "$ROOT/python/ados/main.py"

echo
echo "Command Router Installed."
echo

