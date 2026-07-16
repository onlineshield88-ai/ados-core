#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 13.1"
echo " Python Symbol Indexer"
echo "======================================"

mkdir -p python/ados/indexer

cat > python/ados/indexer/python_indexer.py <<'PY'
import ast
from pathlib import Path


class PythonIndexer:

    def index(self, root):

        root = Path(root)

        symbols = []

        for file in root.rglob("*.py"):

            if ".git" in file.parts:
                continue

            try:
                tree = ast.parse(
                    file.read_text(encoding="utf-8")
                )
            except Exception:
                continue

            rel = str(file.relative_to(root))

            for node in ast.walk(tree):

                if isinstance(node, ast.ClassDef):

                    symbols.append({
                        "type": "class",
                        "name": node.name,
                        "file": rel,
                        "line": node.lineno,
                    })

                elif isinstance(node, ast.FunctionDef):

                    symbols.append({
                        "type": "function",
                        "name": node.name,
                        "file": rel,
                        "line": node.lineno,
                    })

                elif isinstance(node, ast.Import):

                    for alias in node.names:

                        symbols.append({
                            "type": "import",
                            "name": alias.name,
                            "file": rel,
                            "line": node.lineno,
                        })

                elif isinstance(node, ast.ImportFrom):

                    module = node.module or ""

                    symbols.append({
                        "type": "from",
                        "name": module,
                        "file": rel,
                        "line": node.lineno,
                    })

        return symbols
PY

cat > python/ados/indexer/__init__.py <<'PY'
from .python_indexer import PythonIndexer
PY

echo
echo "[1] python indexer"
echo "[2] exports"

echo
echo DONE
