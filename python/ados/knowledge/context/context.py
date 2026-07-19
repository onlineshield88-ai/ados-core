class AgentContext:

    def __init__(self):

        self.objective = None

        self.tasks = []

        self.knowledge = {}

        self.memory = {}

        self.reflection = {}

        self.metadata = {}

    def to_dict(self):

        return {
            "objective": self.objective,
            "tasks": self.tasks,
            "knowledge": self.knowledge,
            "memory": self.memory,
            "reflection": self.reflection,
            "metadata": self.metadata,
        }
