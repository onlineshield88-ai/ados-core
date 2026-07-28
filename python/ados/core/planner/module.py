from ados.core.kernel.module import Module

class PlannerModule(Module):

    name = "planner"

    priority = 20

    def supports(self, event):
        return event.name == "chat"

    def handle(self, event):
        print("[Planner] planning...")
        return event
