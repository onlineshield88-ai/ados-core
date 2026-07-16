#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 14.10"
echo " Maintainability Index Analyzer"
echo "======================================"

mkdir -p python/ados/reasoning

cat > python/ados/reasoning/maintainability.py <<'PY'
import ast
import math
from pathlib import Path


class MaintainabilityAnalyzer:

    def __init__(self, kernel):
        self.kernel = kernel

    def _complexity(self, node):

        cc = 1

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
                cc += 1

            elif isinstance(n, ast.BoolOp):
                cc += max(len(n.values) - 1, 1)

            elif isinstance(n, ast.comprehension):
                cc += 1

        return cc

    def analyze(self):

        report = []

        for file in Path(".").rglob("*.py"):

            if ".git" in file.parts:
                continue

            try:
                source = file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )

                tree = ast.parse(source)

            except Exception:
                continue

            loc = max(len(source.splitlines()), 1)

            functions = [
                n for n in ast.walk(tree)
                if isinstance(
                    n,
                    (
                        ast.FunctionDef,
                        ast.AsyncFunctionDef
                    )
                )
            ]

            if functions:
                avg_cc = (
                    sum(
                        self._complexity(f)
                        for f in functions
                    ) / len(functions)
                )
            else:
                avg_cc = 1

            volume = max(loc * avg_cc, 1)

            mi = max(
                0,
                min(
                    100,
                    round(
                        (
                            171
                            - 5.2 * math.log(volume)
                            - 0.23 * avg_cc
                            - 16.2 * math.log(loc)
                        )
                        * 100
                        / 171,
                        2
                    )
                )
            )

            if mi >= 85:
                grade = "A"
            elif mi >= 70:
                grade = "B"
            elif mi >= 55:
                grade = "C"
            elif mi >= 40:
                grade = "D"
            else:
                grade = "E"

            report.append({
                "file": str(file),
                "mi": mi,
                "grade": grade,
                "loc": loc,
                "avg_cc": round(avg_cc,2)
            })

        return sorted(
            report,
            key=lambda x: x["mi"]
        )

    def summary(self):

        report = self.analyze()

        return {
            "files": len(report),
            "average_mi": round(
                sum(x["mi"] for x in report)
                / max(len(report),1),
                2
            ),
            "report": report
        }
PY

grep -q "MaintainabilityAnalyzer" python/ados/reasoning/__init__.py 2>/dev/null || cat >> python/ados/reasoning/__init__.py <<'PY'
from .maintainability import MaintainabilityAnalyzer
PY

echo
echo "[1] maintainability analyzer"
echo "[2] exports"

echo
echo DONE
