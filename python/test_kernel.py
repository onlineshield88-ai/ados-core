from ados.core.kernel.kernel import Kernel
from ados.core.events.event import Event

from ados.core.conversation.module import ConversationModule
from ados.core.planner.module import PlannerModule
from ados.core.memory.module import MemoryModule
from ados.core.router.module import RouterModule
from ados.core.providers.local_provider import LocalProvider
from ados.core.validator.module import ValidatorModule

kernel = Kernel()

kernel.register(ConversationModule())
kernel.register(PlannerModule())
kernel.register(MemoryModule())
kernel.register(RouterModule())
kernel.register(LocalProvider())
kernel.register(ValidatorModule())

kernel.dispatch(
    Event(
        "chat",
        {
            "text":"Buat website kos modern"
        }
    )
)
