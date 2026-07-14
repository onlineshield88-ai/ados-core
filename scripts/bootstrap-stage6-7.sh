#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 6.7"
echo " Research CLI"
echo "======================================"

mkdir -p python/ados/cli

########################################
echo "[1] research cli"

cat > python/ados/cli/research.py <<'PY'
import sys
import subprocess

COMMANDS = {
    "scan": "./scripts/github-scan.sh",
    "graph": "./scripts/build-graph.sh",
    "compare": "./scripts/compare-repositories.sh",
    "features": "./scripts/features.sh",
    "extract": "./scripts/extract-knowledge.sh",
}

def run():

    if len(sys.argv) < 2:
        print("Usage:")
        print("research scan <url>")
        print("research extract")
        print("research graph")
        print("research compare")
        print("research features")
        return

    cmd = sys.argv[1]

    if cmd == "scan":

        if len(sys.argv) < 3:
            print("Repository URL required")
            return

        subprocess.run([COMMANDS["scan"], sys.argv[2]])
        return

    if cmd in COMMANDS:
        subprocess.run([COMMANDS[cmd]])
        return

    print("Unknown command")
PY

########################################
echo "[2] launcher"

cat > scripts/research-cli.sh <<'SH'
#!/usr/bin/env bash

PYTHONPATH=python python3 -m ados.cli.research "$@"
SH

chmod +x scripts/research-cli.sh

echo
echo DONE

