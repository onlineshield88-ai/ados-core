#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 14.0"
echo " Code Reasoning Engine"
echo "======================================"

mkdir -p python/ados/reasoning

cat > python/ados/reasoning/reasoner.py <<'PY'
class CodeReasoner:

    def __init__(self, kernel):
        self.kernel = kernel

    def analyze(self, symbol):

        refs = self.kernel.memory.get("reference_resolver")
        deps = self.kernel.memory.get("dependency_graph")
        symbols = self.kernel.memory.get("symbols")

        definitions = [
            s for s in symbols
            if s["name"] == symbol
        ]

        callers = refs.callers(symbol)

        modules = []

        for d in definitions:

            m = d["file"]

            modules.append({
                "module": m,
                "imports": deps.imports(m)
            })

        return {
            "symbol": symbol,
            "definitions": definitions,
            "callers": callers,
            "modules": modules,
            "risk": self.risk(callers)
        }

    def risk(self, callers):

        n = len(callers)

        if n == 0:
            return "Very Low"

        if n < 3:
            return "Low"

        if n < 8:
            return "Medium"

        if n < 20:
            return "High"

        return "Critical"
PY

cat > python/ados/reasoning/__init__.py <<'PY'
from .reasoner import CodeReasoner
PY

echo
echo "[1] reasoning engine"
echo "[2] exports"

echo
echo DONE
