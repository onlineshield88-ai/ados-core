import ast
from pathlib import Path


class ComplexityAnalyzer:

    def __init__(self, kernel):
        self.kernel = kernel

    def _complexity(self, node):

        score = 1

        for n in ast.walk(node):

            if isinstance(
                n,
                (
                    ast.If,
                    ast.For,
                    ast.AsyncFor,
                    ast.While,
                    ast.Try,
                    ast.ExceptHandler,
                    ast.With,
                    ast.AsyncWith,
                    ast.IfExp,
                    ast.Match,
                ),
            ):
                score += 1

            elif isinstance(n, ast.BoolOp):
                score += max(len(n.values) - 1, 1)

            elif isinstance(n, ast.comprehension):
                score += 1

        return score

    def analyze(self):

        result = []

        for file in Path(".").rglob("*.py"):

            if ".git" in file.parts:
                continue

            try:
                tree = ast.parse(
                    file.read_text(
                        encoding="utf-8",
                        errors="ignore",
                    )
                )
            except Exception:
                continue

            for node in ast.walk(tree):

                if isinstance(
                    node,
                    (
                        ast.FunctionDef,
                        ast.AsyncFunctionDef,
                    ),
                ):

                    score = self._complexity(node)

                    if score <= 5:
                        level = "Low"
                    elif score <= 10:
                        level = "Medium"
                    elif score <= 20:
                        level = "High"
                    else:
                        level = "Critical"

                    result.append(
                        {
                            "name": node.name,
                            "file": str(file),
                            "line": node.lineno,
                            "complexity": score,
                            "risk": level,
                        }
                    )

        return sorted(
            result,
            key=lambda x: (
                -x["complexity"],
                x["file"],
            ),
        )

    def summary(self):

        report = self.analyze()

        return {
            "functions": len(report),
            "high_risk": len(
                [
                    x
                    for x in report
                    if x["risk"] in (
                        "High",
                        "Critical",
                    )
                ]
            ),
            "report": report,
        }
