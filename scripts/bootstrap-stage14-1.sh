#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 14.1"
echo " Change Impact Analyzer"
echo "======================================"

cat > python/ados/reasoning/impact.py <<'PY'
class ChangeImpactAnalyzer:

    def __init__(self, kernel):
        self.kernel = kernel

    def analyze(self, module):

        deps = self.kernel.memory.get("dependency_graph")
        refs = self.kernel.memory.get("reference_resolver")

        imported = deps.imports(module)

        affected = []

        for m in deps.modules():
            try:
                imports = deps.imports(m)
            except Exception:
                imports = []

            for item in imports:
                if module.endswith(item + ".py") or module.endswith(item.replace(".", "/") + ".py"):
                    affected.append(m)

        score = len(affected)

        if score == 0:
            risk = "Very Low"
        elif score < 3:
            risk = "Low"
        elif score < 8:
            risk = "Medium"
        elif score < 15:
            risk = "High"
        else:
            risk = "Critical"

        return {
            "module": module,
            "imports": imported,
            "affected_modules": sorted(set(affected)),
            "risk": risk,
            "reference_count": len(refs.symbols())
        }
PY

grep -q "ChangeImpactAnalyzer" python/ados/reasoning/__init__.py 2>/dev/null || cat >> python/ados/reasoning/__init__.py <<'PY'
from .impact import ChangeImpactAnalyzer
PY

echo
echo "[1] impact analyzer"
echo "[2] exports"

echo
echo DONE
