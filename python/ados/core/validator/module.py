from ados.core.kernel.module import Module

class ValidatorModule(Module):

    name = "validator"

    priority = 90

    def supports(self, event):
        return event.name == "chat"

    def handle(self, event):
        print("[Validator] ok")
        return event
