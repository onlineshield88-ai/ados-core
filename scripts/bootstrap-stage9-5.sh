#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 9.5"
echo " Tool Executor"
echo "======================================"

mkdir -p python/ados/tool

echo "[1] executor"

cat > python/ados/tool/executor.py <<'PY'
class ToolExecutor:

    def __init__(self, registry):
        self.registry = registry

    def execute(self, tool_name, *args, **kwargs):

        tool = self.registry.get(tool_name)

        if tool is None:
            raise ValueError(f"Tool '{tool_name}' not registered")

        if callable(tool):
            return tool(*args, **kwargs)

        if hasattr(tool, "run"):
            return tool.run(*args, **kwargs)

        raise TypeError(f"Tool '{tool_name}' is not executable")
PY

echo "[2] update __init__"

cat > python/ados/tool/__init__.py <<'PY'
from .registry import ToolRegistry
from .executor import ToolExecutor
PY

echo
echo DONE
