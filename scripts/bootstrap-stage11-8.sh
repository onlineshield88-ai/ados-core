#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 11.8"
echo " Agent Context"
echo "======================================"

mkdir -p python/ados/context

cat > python/ados/context/context.py <<'PY'
class AgentContext:

    def __init__(self):

        self.objective = None

        self.tasks = []

        self.knowledge = {}

        self.memory = {}

        self.reflection = {}

        self.metadata = {}

    def to_dict(self):

        return {
            "objective": self.objective,
            "tasks": self.tasks,
            "knowledge": self.knowledge,
            "memory": self.memory,
            "reflection": self.reflection,
            "metadata": self.metadata,
        }
PY

cat > python/ados/context/__init__.py <<'PY'
from .context import AgentContext
PY

echo
echo "[1] context"
echo "[2] exports"

echo
echo DONE
