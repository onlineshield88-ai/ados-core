import argparse

from ados.router.router import dispatch

parser = argparse.ArgumentParser(
    prog="ados"
)

parser.add_argument(
    "command",
    nargs="?",
    default="doctor"
)

parser.add_argument(
    "args",
    nargs="*"
)

a = parser.parse_args()

dispatch(
    a.command,
    a.args
)
