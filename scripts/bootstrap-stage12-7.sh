#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 12.7"
echo " Dispatcher Runtime"
echo "======================================"

mkdir -p python/ados/runtime

cat > python/ados/runtime/dispatcher.py <<'PY'
from ados.router import AgentRouter
from ados.agent import AgentManager


class Dispatcher:

    def __init__(self):

        self.router = AgentRouter()

        self.manager = AgentManager()

    def register_route(self, task_type, agent_name):

        self.router.register(task_type, agent_name)

    def register_agent(self, agent):

        self.manager.register(agent)

    def dispatch(self, task, context):

        agent = self.router.resolve(task)

        if agent is None:
            raise RuntimeError(
                f"No agent registered for task type '{task.metadata.get('type')}'"
            )

        return self.manager.run(agent, context)
PY

cat > python/ados/runtime/__init__.py <<'PY'
from .context import RuntimeContext
from .session import RuntimeSession
from .memory import RuntimeMemory
from .events import EventBus
from .scheduler import RuntimeScheduler
from .integration import RuntimeIntegration
from .objective_runner import ObjectiveRunner
from .dispatcher import Dispatcher
PY

echo
echo "[1] dispatcher runtime"
echo "[2] exports"

echo
echo DONE
