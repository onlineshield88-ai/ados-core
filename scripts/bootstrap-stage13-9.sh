#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 13.9"
echo " Cross Reference Engine"
echo "======================================"

cat > python/ados/search/xref.py <<'PY'
class CrossReference:

    def __init__(self, kernel):
        self.kernel = kernel

    def definition(self, name):

        result = []

        for s in self.kernel.memory.get("symbols"):

            if s["name"] == name:
                result.append(s)

        return result

    def implementations(self, keyword):

        result = []

        keyword = keyword.lower()

        for s in self.kernel.memory.get("symbols"):

            if s["type"] in ("class", "function"):

                if keyword in s["name"].lower():
                    result.append(s)

        return result

    def usages(self, symbol):

        refs = self.kernel.memory.get(
            "reference_resolver"
        )

        return refs.callers(symbol)

    def imports(self, module):

        deps = self.kernel.memory.get(
            "dependency_graph"
        )

        return deps.imports(module)
PY

grep -q "CrossReference" python/ados/search/__init__.py 2>/dev/null || \
cat >> python/ados/search/__init__.py <<'PY'
from .xref import CrossReference
PY

echo
echo "[1] cross reference"
echo "[2] exports"

echo
echo DONE
