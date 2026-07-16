#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 11.1"
echo " Agent Runtime"
echo "======================================"

mkdir -p python/ados/agent

cat > python/ados/agent/base.py <<'PY'
class Agent:

    name="agent"

    def run(self, context):
        raise NotImplementedError
PY

cat > python/ados/agent/registry.py <<'PY'
class AgentRegistry:

    def __init__(self):
        self._agents={}

    def register(self,name,agent):
        self._agents[name]=agent

    def get(self,name):
        return self._agents.get(name)

    def list(self):
        return sorted(self._agents.keys())
PY

cat > python/ados/agent/__init__.py <<'PY'
from .base import Agent
from .registry import AgentRegistry
PY

echo
echo "[1] agent runtime"
echo "[2] registry"

echo
echo DONE
