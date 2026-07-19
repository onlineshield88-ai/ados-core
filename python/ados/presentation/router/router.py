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

    ensure_boot()

    try:

        if command=="workspace":
            from ados.presentation.cli.workspace import run
            return run(args)

        if command=="doctor":
            from ados.presentation.cli.doctor import run
            return run(args)

        if command=="context":
            from ados.presentation.cli.context import run
            return run(args)

        if command=="search":
            from ados.presentation.cli.search import run
            return run(args)

        if command=="index":
            from ados.presentation.cli.index import run
            return run(args)

        if command=="planner":
            from ados.presentation.cli.planner import run
            return run(args)

        print(f"Unknown command: {command}")

    except Exception as e:
        print(e)


__BOOTSTRAPPED=False

def ensure_boot():
    global __BOOTSTRAPPED
    if not __BOOTSTRAPPED:
        from ados.kernel.bootstrap import initialize
        initialize(".")
        __BOOTSTRAPPED = True
