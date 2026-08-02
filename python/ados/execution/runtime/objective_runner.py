from ados.reasoning.agent import AgentManager
from ados.reasoning.agent import AgentLoader
from ados.execution.runtime import RuntimeIntegration


class ObjectiveRunner:

    def __init__(self):

        self.manager = AgentManager()

        AgentLoader(self.manager).load()

    def run(self, objective):

        context = {
            "objective": objective
        }

        self.manager.run("planner", context)

        runtime = RuntimeIntegration()

        runtime.load_tasks(context["tasks"])

        completed = runtime.execute()

        context["completed"] = completed

        return context
