class AgentRouter:

    def __init__(self):
        self.routes = {}

    def register(self, task_type, agent_name):
        self.routes[task_type] = agent_name

    def resolve(self, task):

        t = task.metadata.get("type")

        return self.routes.get(t)
