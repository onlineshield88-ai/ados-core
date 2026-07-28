from ados.core.kernel.module import Module

class LocalProvider(Module):

    name = "local-qwen"

    priority = 50

    def supports(self, event):
        return event.name == "chat"

    def handle(self, event):
        print("[Local Qwen] placeholder")
        return event
