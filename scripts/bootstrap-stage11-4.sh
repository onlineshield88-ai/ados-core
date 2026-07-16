#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 11.4"
echo " Kernel Agent Integration"
echo "======================================"

cat > python/ados/kernel/agent_runtime.py <<'PY'
from ados.agent import AgentManager
from ados.agent import AgentLoader


class AgentRuntime:

    def __init__(self):

        self.manager = AgentManager()

        AgentLoader(
            self.manager
        ).load()

    def run(self, name, context):

        return self.manager.run(
            name,
            context
        )

    def list(self):

        return self.manager.list()
PY


cat > python/ados/kernel/__init__.py <<'PY'
from .bootstrap import initialize
from .bootstrap import kernel

from .kernel import ADOSKernel
from .container import ServiceContainer
from .agent_runtime import AgentRuntime
PY


echo
echo "[1] kernel runtime"
echo "[2] exports"

echo
echo DONE
