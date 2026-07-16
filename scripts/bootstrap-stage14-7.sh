#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 14.7"
echo " Unused Import Detector"
echo "======================================"

mkdir -p python/ados/reasoning

cat > python/ados/reasoning/unused_imports.py <<'PY'
import ast
from pathlib import Path


class UnusedImportDetector:

    def __init__(self, kernel):
        self.kernel = kernel

    def detect(self):

        result = []

        root = Path(".")

        for file in root.rglob("*.py"):

            if ".git" in file.parts:
                continue

            try:
                tree = ast.parse(
                    file.read_text(
                        encoding="utf-8",
                        errors="ignore"
                    )
                )
            except Exception:
                continue

            imports = {}
            used = set()

            for node in ast.walk(tree):

                if isinstance(node, ast.Import):
                    for alias in node.names:
                        name = alias.asname or alias.name.split(".")[0]
                        imports[name] = (
                            alias.name,
                            node.lineno
                        )

                elif isinstance(node, ast.ImportFrom):
                    for alias in node.names:
                        name = alias.asname or alias.name
                        imports[name] = (
                            alias.name,
                            node.lineno
                        )

                elif isinstance(node, ast.Name):
                    used.add(node.id)

            for local_name, (real_name, line) in imports.items():

                if local_name not in used:

                    result.append({
                        "file": str(file),
                        "line": line,
                        "import": real_name
                    })

        return sorted(
            result,
            key=lambda x: (
                x["file"],
                x["line"]
            )
        )

    def summary(self):

        unused = self.detect()

        return {
            "unused_imports": len(unused),
            "imports": unused
        }
PY

grep -q "UnusedImportDetector" python/ados/reasoning/__init__.py 2>/dev/null || cat >> python/ados/reasoning/__init__.py <<'PY'
from .unused_imports import UnusedImportDetector
PY

echo
echo "[1] unused import detector"
echo "[2] exports"

echo
echo DONE
