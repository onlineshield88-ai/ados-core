class AgentPipeline:

    def __init__(self, manager):
        self.manager = manager
        self.steps = []

    def add(self, agent):

        self.steps.append(agent)

    def run(self, context):

        for step in self.steps:
            self.manager.run(step, context)

        return context
