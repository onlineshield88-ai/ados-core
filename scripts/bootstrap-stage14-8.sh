#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 14.8"
echo " Code Smell Detector"
echo "======================================"

mkdir -p python/ados/reasoning

cat > python/ados/reasoning/smells.py <<'PY'
import ast
from pathlib import Path


class CodeSmellDetector:

    def __init__(self, kernel):
        self.kernel = kernel

    def detect(self):

        result = []

        for file in Path(".").rglob("*.py"):

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

            for node in ast.walk(tree):

                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):

                    body = len(node.body)

                    args = len(node.args.args)

                    if body > 40:
                        result.append({
                            "type": "Long Function",
                            "name": node.name,
                            "file": str(file),
                            "line": node.lineno,
                            "value": body
                        })

                    if args > 6:
                        result.append({
                            "type": "Too Many Parameters",
                            "name": node.name,
                            "file": str(file),
                            "line": node.lineno,
                            "value": args
                        })

                elif isinstance(node, ast.ClassDef):

                    methods = sum(
                        isinstance(
                            x,
                            (
                                ast.FunctionDef,
                                ast.AsyncFunctionDef
                            )
                        )
                        for x in node.body
                    )

                    if methods > 15:
                        result.append({
                            "type": "Large Class",
                            "name": node.name,
                            "file": str(file),
                            "line": node.lineno,
                            "value": methods
                        })

        return sorted(
            result,
            key=lambda x: (
                x["file"],
                x["line"]
            )
        )

    def summary(self):

        smells = self.detect()

        return {
            "total": len(smells),
            "smells": smells
        }
PY

grep -q "CodeSmellDetector" python/ados/reasoning/__init__.py 2>/dev/null || cat >> python/ados/reasoning/__init__.py <<'PY'
from .smells import CodeSmellDetector
PY

echo
echo "[1] code smell detector"
echo "[2] exports"

echo
echo DONE
