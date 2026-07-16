#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 11.3"
echo " Agent Auto Loader"
echo "======================================"

mkdir -p python/ados/agents

cat > python/ados/agent/loader.py <<'PY'
import pkgutil
import importlib


class AgentLoader:

    def __init__(self, manager):
        self.manager = manager

    def load(self):

        import ados.agents

        for _, module_name, _ in pkgutil.iter_modules(
            ados.agents.__path__
        ):

            module = importlib.import_module(
                f"ados.agents.{module_name}"
            )

            if hasattr(module, "agent"):

                self.manager.register(
                    module.agent
                )
PY


cat > python/ados/agents/__init__.py <<'PY'
# ADOS Agents Package
PY


cat > python/ados/agents/planner.py <<'PY'
from ados.agent import Agent


class PlannerAgent(Agent):

    name = "planner"

    def run(self, context):

        context["planned"] = True

        return context


agent = PlannerAgent()
PY


cat > python/ados/agent/__init__.py <<'PY'
from .base import Agent
from .registry import AgentRegistry
from .manager import AgentManager
from .loader import AgentLoader
PY


echo
echo "[1] loader"
echo "[2] planner agent"

echo
echo DONE
