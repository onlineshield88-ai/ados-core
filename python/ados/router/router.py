import ados.router.bootstrap

from ados.router.registry import (
    get,
    all_commands,
)


def dispatch(command, args):

    fn = get(command)

    if fn is None:

        print("Unknown command:", command)
        print()
        print("Available commands:")

        for c in all_commands():
            print(" ", c)

        return

    fn(args)
