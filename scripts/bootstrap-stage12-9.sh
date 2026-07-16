#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 12.9"
echo " Workspace Scanner"
echo "======================================"

mkdir -p python/ados/workspace

cat > python/ados/workspace/scanner.py <<'PY'
from pathlib import Path


class WorkspaceScanner:

    def scan(self, root):

        root = Path(root)

        result = {
            "root": str(root.resolve()),
            "directories": [],
            "files": [],
        }

        for item in root.rglob("*"):

            if ".git" in item.parts:
                continue

            if item.is_dir():
                result["directories"].append(
                    str(item.relative_to(root))
                )
            else:
                result["files"].append(
                    str(item.relative_to(root))
                )

        result["directory_count"] = len(result["directories"])
        result["file_count"] = len(result["files"])

        return result
PY

cat > python/ados/workspace/__init__.py <<'PY'
from .scanner import WorkspaceScanner
PY

echo
echo "[1] workspace scanner"
echo "[2] exports"

echo
echo DONE
