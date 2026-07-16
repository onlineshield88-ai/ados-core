from ados.runtime import (
    RuntimeContext,
    RuntimeSession,
    RuntimeMemory,
    RuntimeScheduler,
    EventBus,
)

from ados.capability import CapabilityManager
from .container import ServiceContainer
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
