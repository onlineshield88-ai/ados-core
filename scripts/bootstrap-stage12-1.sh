#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 12.1"
echo " Dependency Resolver"
echo "======================================"

mkdir -p python/ados/resolver

cat > python/ados/resolver/dependency.py <<'PY'
class DependencyResolver:

    def __init__(self, graph):
        self.graph = graph
        self.completed = set()

    def complete(self, task_id):
        self.completed.add(task_id)

    def ready(self):

        ready = []

        for task in self.graph.tasks():

            if task.id in self.completed:
                continue

            deps = task.depends_on

            if all(d in self.completed for d in deps):
                ready.append(task)

        return ready
PY

cat > python/ados/resolver/__init__.py <<'PY'
from .dependency import DependencyResolver
PY

echo
echo "[1] dependency resolver"
echo "[2] exports"

echo
echo DONE
