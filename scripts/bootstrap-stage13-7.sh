#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 13.7"
echo " Repository Intelligence Engine"
echo "======================================"

mkdir -p python/ados/intelligence

cat > python/ados/intelligence/repository.py <<'PY'
class RepositoryIntelligence:

    def __init__(self, kernel):

        self.kernel = kernel

    def summary(self):

        repo = self.kernel.memory.get("repository")
        symbols = self.kernel.memory.get("symbols")
        deps = self.kernel.memory.get("dependency_graph")
        refs = self.kernel.memory.get("reference_resolver")

        return {
            "files": repo["total_files"],
            "languages": repo["languages"],
            "symbols": len(symbols),
            "modules": deps.size(),
            "references": len(refs.symbols())
        }

    def callers(self, symbol):

        refs = self.kernel.memory.get(
            "reference_resolver"
        )

        return refs.callers(symbol)

    def modules(self):

        deps = self.kernel.memory.get(
            "dependency_graph"
        )

        return deps.modules()

    def imports(self, module):

        deps = self.kernel.memory.get(
            "dependency_graph"
        )

        return deps.imports(module)
PY

cat > python/ados/intelligence/__init__.py <<'PY'
from .repository import RepositoryIntelligence
PY

echo
echo "[1] repository intelligence"
echo "[2] exports"

echo
echo DONE
