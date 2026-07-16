#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 13.3"
echo " Dependency Graph"
echo "======================================"

mkdir -p python/ados/graph

cat > python/ados/graph/dependency_graph.py <<'PY'
from collections import defaultdict


class DependencyGraph:

    def __init__(self):

        self._graph = defaultdict(set)

    def build(self, symbols):

        self._graph.clear()

        current = None

        for s in symbols:

            if s["type"] == "class":
                current = s["file"]

            elif s["type"] == "function":
                current = s["file"]

            elif s["type"] in ("import", "from"):

                if current is None:
                    current = s["file"]

                self._graph[current].add(s["name"])

    def modules(self):

        return sorted(self._graph.keys())

    def imports(self, module):

        return sorted(self._graph.get(module, []))

    def size(self):

        return len(self._graph)
PY

cat > python/ados/graph/__init__.py <<'PY'
from .task_graph import TaskGraph
from .dependency_graph import DependencyGraph
PY

echo
echo "[1] dependency graph"
echo "[2] exports"

echo
echo DONE
