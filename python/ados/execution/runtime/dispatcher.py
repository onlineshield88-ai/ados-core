from ados.presentation.router import AgentRouter
from ados.reasoning.agent import AgentManager


class Dispatcher:

    def __init__(self):

        self.router = AgentRouter()

        self.manager = AgentManager()

    def register_route(self, task_type, agent_name):

        self.router.register(task_type, agent_name)

    def register_agent(self, agent):

        self.manager.register(agent)

    def dispatch(self, task, context):

        agent = self.router.resolve(task)

        if agent is None:
            raise RuntimeError(
                f"No agent registered for task type '{task.metadata.get('type')}'"
            )

        return self.manager.run(agent, context)
