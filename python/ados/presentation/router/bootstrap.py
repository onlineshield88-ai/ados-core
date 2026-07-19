from ados.presentation.router.registry import register

from ados.presentation.cli.doctor import run as doctor
from ados.presentation.cli.workspace import run as workspace
from ados.presentation.cli.research import run as research
from ados.presentation.cli.architecture import run as architecture
from ados.presentation.cli.framework import run as framework
from ados.presentation.cli.dependency import run as dependency

register("doctor", doctor)
register("workspace", workspace)
register("research", research)
register("architecture", architecture)
register("framework", framework)
register("dependency", dependency)
