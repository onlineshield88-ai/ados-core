import pkgutil
import importlib


class AgentLoader:

    def __init__(self, manager):
        self.manager = manager

    def load(self):

        import ados.agents

        for _, module_name, _ in pkgutil.iter_modules(
            ados.agents.__path__
        ):

            module = importlib.import_module(
                f"ados.agents.{module_name}"
            )

            if hasattr(module, "agent"):

                self.manager.register(
                    module.agent
                )
