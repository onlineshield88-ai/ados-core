#!/data/data/com.termux/files/usr/bin/bash
set -e

mkdir -p python/tests

cat > python/pyproject.toml <<'PY'
[project]
name = "ados"
version = "0.2.0-alpha"
description = "ADOS Python Runtime"
requires-python = ">=3.10"
PY

cat > python/README.md <<'DOC'
# ADOS Python Runtime

This directory contains the Python runtime for ADOS.

Modules:

- Workspace
- GitHub
- Products
- Templates
- Database
DOC

cat > python/ados/main.py <<'PY'
#!/usr/bin/env python3

import sys

def banner():
    print("=" * 40)
    print("ADOS Python Runtime")
    print("Version : 0.2.0-alpha")
    print("=" * 40)

def main():
    banner()

    if len(sys.argv) == 1:
        print("Usage:")
        print("  ados workspace scan")
        return

    print("Arguments:", sys.argv[1:])

if __name__ == "__main__":
    main()
PY

chmod +x python/ados/main.py

echo
echo "Python Runtime Installed."
echo

tree python
