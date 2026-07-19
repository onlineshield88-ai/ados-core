from ados.knowledge.workspace.workspace import Workspace


def run(args=None):

    if args is None:
        args = []

    if len(args) == 0:
        print("workspace commands:")
        print(" scan")
        return

    cmd = args[0]

    if cmd == "scan":
        Workspace().scan()
        return

    print("Unknown workspace command")
