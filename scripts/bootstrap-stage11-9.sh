#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 11.9"
echo " Task Graph"
echo "======================================"

mkdir -p python/ados/graph

cat > python/ados/graph/task_graph.py <<'PY'
class TaskGraph:

    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_task(self, task):
        self.nodes[task.id] = task
        self.edges.setdefault(task.id, [])

    def connect(self, parent, child):
        self.edges.setdefault(parent, [])
        self.edges[parent].append(child)

    def children(self, task_id):
        return self.edges.get(task_id, [])

    def tasks(self):
        return list(self.nodes.values())
PY

cat > python/ados/graph/__init__.py <<'PY'
from .task_graph import TaskGraph
PY

echo
echo "[1] task graph"
echo "[2] exports"

echo
echo DONE
