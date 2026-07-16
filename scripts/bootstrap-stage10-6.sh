#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 10.6"
echo " ADOS Kernel"
echo "======================================"

mkdir -p python/ados/kernel

cat > python/ados/kernel/kernel.py <<'PY'
from ados.runtime import (
    RuntimeContext,
    RuntimeSession,
    RuntimeMemory,
    RuntimeScheduler,
    EventBus,
)

from ados.capability import CapabilityManager
from ados.kernel.container import ServiceContainer
from ados.tool import ToolRegistry


class ADOSKernel:

    def __init__(self):

        self.context = RuntimeContext()
        self.session = RuntimeSession()
        self.memory = RuntimeMemory()
        self.scheduler = RuntimeScheduler()
        self.events = EventBus()

        self.capabilities = CapabilityManager()
        self.services = ServiceContainer()
        self.tools = ToolRegistry()

    def info(self):

        return {
            "session": self.session.id,
            "services": self.services.list(),
            "tools": self.tools.list(),
            "memory": self.memory.keys(),
            "pending": self.scheduler.pending(),
        }
PY

cat > python/ados/kernel/__init__.py <<'PY'
from .kernel import ADOSKernel
from .container import ServiceContainer
PY

echo
echo "[1] kernel"
echo "[2] exports"

echo
echo "DONE"
