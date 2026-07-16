#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 13.8"
echo " Semantic Search Engine"
echo "======================================"

mkdir -p python/ados/search

cat > python/ados/search/search.py <<'PY'
class SemanticSearch:

    def __init__(self, kernel):
        self.kernel = kernel

    def symbols(self, keyword):

        keyword = keyword.lower()

        results = []

        for s in self.kernel.memory.get("symbols"):

            if keyword in s["name"].lower():
                results.append(s)

        return results

    def modules(self, keyword):

        deps = self.kernel.memory.get(
            "dependency_graph"
        )

        keyword = keyword.lower()

        return [
            m
            for m in deps.modules()
            if keyword in m.lower()
        ]

    def callers(self, symbol):

        refs = self.kernel.memory.get(
            "reference_resolver"
        )

        return refs.callers(symbol)
PY

cat > python/ados/search/__init__.py <<'PY'
from .search import SemanticSearch
PY

echo
echo "[1] semantic search"
echo "[2] exports"

echo
echo DONE
