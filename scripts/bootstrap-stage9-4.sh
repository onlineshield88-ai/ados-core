#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 9.4"
echo " Tool Registry"
echo "======================================"

mkdir -p python/ados/tool

echo "[1] registry"

cat > python/ados/tool/__init__.py <<'PY'
from .registry import ToolRegistry
PY

cat > python/ados/tool/registry.py <<'PY'
class ToolRegistry:

    def __init__(self):
        self.tools = {}

    def register(self, name, tool):
        self.tools[name] = tool

    def unregister(self, name):
        self.tools.pop(name, None)

    def get(self, name):
        return self.tools.get(name)

    def list(self):
        return sorted(self.tools.keys())
PY

echo "[2] done"

echo
echo DONE
