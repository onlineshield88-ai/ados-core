class AgentRouter:

    def __init__(self):
        self.routes = {}

    def register(self, task_type, agent_name):
        self.routes[task_type] = agent_name

    def resolve(self, task):

        t = task.metadata.get("type")

        return self.routes.get(t)


def dispatch(command,args=None):
    """
    Universal command dispatcher.
    """

    args=args or []

    try:

        if command=="workspace":
            from ados.cli.workspace import run
            return run(args)

        if command=="doctor":
            from ados.cli.doctor import run
            return run(args)

        if command=="context":
            from ados.cli.context import run
            return run(args)

        if command=="planner":
            from ados.cli.planner import run
            return run(args)

        print(f"Unknown command: {command}")

    except Exception as e:
        print(e)
