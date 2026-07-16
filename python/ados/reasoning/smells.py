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
