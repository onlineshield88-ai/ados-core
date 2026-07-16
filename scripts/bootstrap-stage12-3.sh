#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 12.3"
echo " Execution Engine"
echo "======================================"

mkdir -p python/ados/execution

cat > python/ados/execution/engine.py <<'PY'
from ados.execution import TaskExecutor


class ExecutionEngine:

    def __init__(self, queue):

        self.executor = TaskExecutor(queue)

    def execute(self):

        results = []

        def worker(task):

            task.status = "completed"

            results.append(task)

            return task

        self.executor.run(worker)

        return results
PY

cat > python/ados/execution/__init__.py <<'PY'
from .executor import TaskExecutor
from .engine import ExecutionEngine
PY

echo
echo "[1] execution engine"
echo "[2] exports"

echo
echo DONE
