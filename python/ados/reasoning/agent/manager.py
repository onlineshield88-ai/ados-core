from .registry import AgentRegistry


class AgentManager:

    def __init__(self):
        self.registry = AgentRegistry()

    def register(self, agent):
        self.registry.register(agent.name, agent)

    def get(self, name):
        return self.registry.get(name)

    def list(self):
        return self.registry.list()

    def run(self, name, context):

        agent = self.get(name)

        if agent is None:
            raise ValueError(f"Unknown agent: {name}")

        return agent.run(context)
