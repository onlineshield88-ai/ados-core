#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 11.2"
echo " Agent Manager"
echo "======================================"

mkdir -p python/ados/agent

cat > python/ados/agent/manager.py <<'PY'
from .registry import AgentRegistry


class AgentManager:

    def __init__(self):
        self.registry = AgentRegistry()

    def register(self, agent):
        self.registry.register(agent.name, agent)

    def get(self, name):
        return self.registry.get(name)

    def list(self):
        return self.registry.list()

    def run(self, name, context):

        agent = self.get(name)

        if agent is None:
            raise ValueError(f"Unknown agent: {name}")

        return agent.run(context)
PY

cat > python/ados/agent/__init__.py <<'PY'
from .base import Agent
from .registry import AgentRegistry
from .manager import AgentManager
PY

echo
echo "[1] manager"
echo "[2] exports"

echo
echo DONE
