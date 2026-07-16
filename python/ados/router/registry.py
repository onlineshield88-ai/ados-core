from ados.cli.doctor import run as doctor
from ados.cli.workspace import run as workspace
from ados.cli.research import run as research
from ados.cli.framework import run as framework
from ados.cli.dependency import run as dependency
from ados.cli.architecture import run as architecture
from ados.cli.planner import run as planner

REGISTRY = {}


def register(name, handler):
    REGISTRY[name] = handler


def unregister(name):
    REGISTRY.pop(name, None)


def get(name):
    return REGISTRY.get(name)


def all_commands():
    return sorted(REGISTRY.keys())


COMMANDS = {
    "doctor": doctor,
    "workspace": workspace,
    "research": research,
    "framework": framework,
    "dependency": dependency,
    "architecture": architecture,
    "planner": planner,
}

for name, handler in COMMANDS.items():
    register(name, handler)
