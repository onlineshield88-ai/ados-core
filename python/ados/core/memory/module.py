from ados.core.kernel.module import Module

class MemoryModule(Module):

    name = "memory"

    priority = 30

    def supports(self, event):
        return event.name == "chat"

    def handle(self, event):
        print("[Memory] loading...")
        return event
