from ados.router.registry import register

from ados.cli.doctor import run as doctor
from ados.cli.workspace import run as workspace
from ados.cli.research import run as research
from ados.cli.architecture import run as architecture
from ados.cli.framework import run as framework
from ados.cli.dependency import run as dependency

register("doctor", doctor)
register("workspace", workspace)
register("research", research)
register("architecture", architecture)
register("framework", framework)
register("dependency", dependency)
