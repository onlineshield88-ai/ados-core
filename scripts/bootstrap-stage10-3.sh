#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 10.3"
echo " Runtime Memory"
echo "======================================"

mkdir -p python/ados/runtime

cat > python/ados/runtime/memory.py <<'PY'
class RuntimeMemory:

    def __init__(self):
        self._memory = {}

    def put(self, key, value):
        self._memory[key] = value

    def get(self, key, default=None):
        return self._memory.get(key, default)

    def delete(self, key):
        self._memory.pop(key, None)

    def clear(self):
        self._memory.clear()

    def keys(self):
        return list(self._memory.keys())

    def dump(self):
        return dict(self._memory)
PY

cat > python/ados/runtime/__init__.py <<'PY'
from .doctor import doctor
from .context import RuntimeContext
from .session import RuntimeSession
from .memory import RuntimeMemory
PY

echo
echo "[1] runtime memory"
echo "[2] exports"
echo
echo "DONE"
