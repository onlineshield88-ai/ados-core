from ados.core.kernel.module import Module

class ConversationModule(Module):

    name = "conversation"

    priority = 10

    def supports(self, event):
        return event.name == "chat"

    def handle(self, event):
        print("[Conversation]", event.payload.get("text"))
        return event
