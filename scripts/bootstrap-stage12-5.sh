#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 12.5"
echo " Runtime Integration"
echo "======================================"

mkdir -p python/ados/runtime

cat > python/ados/runtime/integration.py <<'PY'
from ados.graph import TaskGraph
from ados.queue import TaskQueue
from ados.resolver import DependencyResolver
from ados.execution import ExecutionEngine


class RuntimeIntegration:

    def __init__(self):

        self.graph = TaskGraph()

        self.queue = TaskQueue()

    def load_tasks(self, tasks):

        for task in tasks:
            self.graph.add_task(task)

        resolver = DependencyResolver(self.graph)

        while True:

            ready = resolver.ready()

            if not ready:
                break

            for task in ready:

                self.queue.push(task)

                resolver.complete(task.id)

    def execute(self):

        engine = ExecutionEngine(self.queue)

        return engine.execute()
PY

cat > python/ados/runtime/__init__.py <<'PY'
from .context import RuntimeContext
from .session import RuntimeSession
from .memory import RuntimeMemory
from .events import EventBus
from .scheduler import RuntimeScheduler
from .integration import RuntimeIntegration
PY

echo
echo "[1] runtime integration"
echo "[2] exports"

echo
echo DONE
