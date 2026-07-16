#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 14.11"
echo " Repository Health Analyzer"
echo "======================================"

mkdir -p python/ados/reasoning

cat > python/ados/reasoning/health.py <<'PY'
class RepositoryHealthAnalyzer:

    def __init__(self, kernel):
        self.kernel = kernel

    def analyze(self):

        complexity = self.kernel.memory.get("complexity_summary")
        maintainability = self.kernel.memory.get("maintainability_summary")
        deadcode = self.kernel.memory.get("deadcode_summary")
        unused = self.kernel.memory.get("unused_imports_summary")
        cycles = self.kernel.memory.get("cycle_summary")

        high_risk = complexity["high_risk"]
        avg_mi = maintainability["average_mi"]
        dead = deadcode["dead_symbols"]
        unused_imports = unused["unused_imports"]
        cycle_count = cycles["cycle_count"]

        score = 100

        score -= high_risk * 2
        score -= dead * 0.10
        score -= unused_imports * 0.20
        score -= cycle_count * 5
        score += (avg_mi - 70) * 0.5

        score = max(0, min(100, round(score,2)))

        if score >= 90:
            grade = "A+"
        elif score >= 80:
            grade = "A"
        elif score >= 70:
            grade = "B"
        elif score >= 60:
            grade = "C"
        elif score >= 50:
            grade = "D"
        else:
            grade = "E"

        return {
            "score": score,
            "grade": grade,
            "high_risk_functions": high_risk,
            "dead_symbols": dead,
            "unused_imports": unused_imports,
            "cycles": cycle_count,
            "maintainability": avg_mi,
        }
PY

grep -q "RepositoryHealthAnalyzer" python/ados/reasoning/__init__.py 2>/dev/null || cat >> python/ados/reasoning/__init__.py <<'PY'
from .health import RepositoryHealthAnalyzer
PY

python3 <<'PY'
from pathlib import Path

boot = Path("python/ados/kernel/bootstrap.py")

text = boot.read_text()

insert = '''

from ados.reasoning import (
    ComplexityAnalyzer,
    MaintainabilityAnalyzer,
    DeadCodeDetector,
    UnusedImportDetector,
    CircularDependencyDetector,
)

k.memory.put(
    "complexity_summary",
    ComplexityAnalyzer(k).summary()
)

k.memory.put(
    "maintainability_summary",
    MaintainabilityAnalyzer(k).summary()
)

k.memory.put(
    "deadcode_summary",
    DeadCodeDetector(k).summary()
)

k.memory.put(
    "unused_imports_summary",
    UnusedImportDetector(k).summary()
)

k.memory.put(
    "cycle_summary",
    CircularDependencyDetector(k).summary()
)
'''

if "complexity_summary" not in text:
    idx = text.rfind("return k")
    text = text[:idx] + insert + "\n" + text[idx:]
    boot.write_text(text)

print("bootstrap updated")
PY

echo
echo "[1] repository health analyzer"
echo "[2] kernel integration"
echo
echo DONE
