from ados.reasoning.agent import AgentManager
from ados.reasoning.agent import AgentLoader


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
