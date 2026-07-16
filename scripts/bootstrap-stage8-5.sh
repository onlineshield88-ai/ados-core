#!/data/data/com.termux/files/usr/bin/bash

echo "======================================"
echo " ADOS STAGE 8.5"
echo " Task Executor"
echo "======================================"

mkdir -p python/ados/executor

cat > python/ados/executor/__init__.py <<'PY'
from .executor import Executor
PY

cat > python/ados/executor/executor.py <<'PY'
class Executor:

    def __init__(self):
        self.handlers = {}

    def register(self, task_type, handler):
        self.handlers[task_type] = handler

    def execute(self, task):

        handler = self.handlers.get(task.metadata.get("type"))

        if handler is None:
            print("No executor:", task.metadata.get("type"))
            return

        return handler(task)

    def list(self):
        return sorted(self.handlers.keys())
PY

echo "[1] executor"
echo "[2] init"

echo
echo DONE
