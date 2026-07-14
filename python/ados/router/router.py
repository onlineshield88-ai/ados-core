from ados.cli.workspace import run as workspace
from ados.cli.state import run as state

COMMANDS = {
    "workspace": workspace,
    "state": state,
}

def dispatch(argv):

    if len(argv) < 2:
        print("")
        print("ADOS Commands")
        print("")
        for cmd in sorted(COMMANDS.keys()):
            print(" ", cmd)
        return

    command = argv[1]

    if command not in COMMANDS:
        print("Unknown command:", command)
        return

    COMMANDS[command](argv[2:])
