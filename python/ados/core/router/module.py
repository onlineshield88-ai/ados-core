from ados.core.kernel.module import Module

class RouterModule(Module):

    name = "router"

    priority = 40

    def supports(self, event):
        return event.name == "chat"

    def handle(self, event):
        print("[Router] selecting provider...")
        return event
