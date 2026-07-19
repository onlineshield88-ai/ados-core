import importlib

MODULES = (
    "ados.agents.planner",
    "ados.agents.knowledge",
)


class AgentLoader:

    def __init__(self, manager):
        self.manager = manager

    def load(self):

        for module_name in MODULES:

            module = importlib.import_module(module_name)

            self.manager.register(module.agent)
