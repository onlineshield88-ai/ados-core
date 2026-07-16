#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 12.6"
echo " Objective Runner"
echo "======================================"

mkdir -p python/ados/runtime

cat > python/ados/runtime/objective_runner.py <<'PY'
from ados.agent import AgentManager
from ados.agent import AgentLoader
from ados.runtime import RuntimeIntegration


class ObjectiveRunner:

    def __init__(self):

        self.manager = AgentManager()

        AgentLoader(self.manager).load()

    def run(self, objective):

        context = {
            "objective": objective
        }

        self.manager.run("planner", context)

        runtime = RuntimeIntegration()

        runtime.load_tasks(context["tasks"])

        completed = runtime.execute()

        context["completed"] = completed

        return context
PY

cat > python/ados/runtime/__init__.py <<'PY'
from .context import RuntimeContext
from .session import RuntimeSession
from .memory import RuntimeMemory
from .events import EventBus
from .scheduler import RuntimeScheduler
from .integration import RuntimeIntegration
from .objective_runner import ObjectiveRunner
PY

echo
echo "[1] objective runner"
echo "[2] exports"

echo
echo DONE
