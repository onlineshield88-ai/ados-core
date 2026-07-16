#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 14.3"
echo " Architecture Dependency Analyzer"
echo "======================================"

mkdir -p python/ados/reasoning

cat > python/ados/reasoning/architecture.py <<'PY'
class ArchitectureAnalyzer:

    def __init__(self, kernel):
        self.kernel = kernel

    def analyze(self):

        deps = self.kernel.memory.get(
            "dependency_graph"
        )

        report = []

        for module in sorted(deps.modules()):

            try:
                imports = deps.imports(module)
            except Exception:
                imports = []

            report.append({
                "module": module,
                "imports": len(imports),
                "dependencies": sorted(imports)
            })

        return report

    def hotspots(self):

        report = self.analyze()

        return sorted(
            report,
            key=lambda x: x["imports"],
            reverse=True
        )

    def summary(self):

        report = self.analyze()

        total_imports = sum(
            item["imports"]
            for item in report
        )

        return {
            "modules": len(report),
            "total_imports": total_imports,
            "average_imports":
                round(
                    total_imports / max(len(report),1),
                    2
                )
        }
PY

grep -q "ArchitectureAnalyzer" python/ados/reasoning/__init__.py 2>/dev/null || cat >> python/ados/reasoning/__init__.py <<'PY'
from .architecture import ArchitectureAnalyzer
PY

echo
echo "[1] architecture analyzer"
echo "[2] exports"

echo
echo DONE
