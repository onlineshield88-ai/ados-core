#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 12.2"
echo " Task Executor Engine"
echo "======================================"

mkdir -p python/ados/execution

cat > python/ados/execution/executor.py <<'PY'
class TaskExecutor:

    def __init__(self, queue):

        self.queue = queue

    def run(self, callback):

        results = []

        while not self.queue.empty():

            task = self.queue.pop()

            results.append(callback(task))

        return results
PY

cat > python/ados/execution/__init__.py <<'PY'
from .executor import TaskExecutor
PY

echo
echo "[1] task executor"
echo "[2] exports"

echo
echo DONE
