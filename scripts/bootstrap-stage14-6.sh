#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 14.6"
echo " Dead Code Detector"
echo "======================================"

mkdir -p python/ados/reasoning

cat > python/ados/reasoning/deadcode.py <<'PY'
class DeadCodeDetector:

    def __init__(self, kernel):
        self.kernel = kernel

    def detect(self):

        refs = self.kernel.memory.get(
            "reference_resolver"
        )

        symbols = self.kernel.memory.get(
            "symbols"
        )

        result = []

        for symbol in symbols:

            if symbol["type"] not in (
                "class",
                "function"
            ):
                continue

            callers = refs.callers(
                symbol["name"]
            )

            callers = [
                c for c in callers
                if c != symbol["file"]
            ]

            if not callers:
                result.append({
                    "name": symbol["name"],
                    "type": symbol["type"],
                    "file": symbol["file"],
                    "line": symbol["line"]
                })

        return sorted(
            result,
            key=lambda x: (
                x["file"],
                x["line"]
            )
        )

    def summary(self):

        dead = self.detect()

        return {
            "dead_symbols": len(dead),
            "symbols": dead
        }
PY

grep -q "DeadCodeDetector" python/ados/reasoning/__init__.py 2>/dev/null || cat >> python/ados/reasoning/__init__.py <<'PY'
from .deadcode import DeadCodeDetector
PY

echo
echo "[1] dead code detector"
echo "[2] exports"

echo
echo DONE
