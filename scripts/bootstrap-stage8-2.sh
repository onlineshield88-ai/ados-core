#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 8.2"
echo " Capability Manager"
echo "======================================"

mkdir -p \
python/ados/capability

echo "[1] capability manager"

cat > python/ados/capability/manager.py <<'PY'
class CapabilityManager:

    def __init__(self):
        self.capabilities = {}

    def register(self, name, handler):
        self.capabilities[name] = handler

    def unregister(self, name):
        self.capabilities.pop(name, None)

    def get(self, name):
        return self.capabilities.get(name)

    def list(self):
        return sorted(self.capabilities.keys())
PY

echo "[2] init"

cat > python/ados/capability/__init__.py <<'PY'
from .manager import CapabilityManager
PY

echo
echo DONE
