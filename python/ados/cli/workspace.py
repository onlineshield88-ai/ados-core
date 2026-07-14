from ados.workspace.workspace import Workspace

def run(args):

    if not args:
        print("workspace commands:")
        print(" scan")
        return

    if args[0] == "scan":
        Workspace().scan()
        return

    print("Unknown workspace command")
