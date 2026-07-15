#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 7.5"
echo " Dynamic Command Registry"
echo "======================================"

mkdir -p python/ados/router

#################################################

echo "[1] registry"

cat > python/ados/router/registry.py <<'PY'
REGISTRY = {}

def register(name, handler):
    REGISTRY[name] = handler

def unregister(name):
    REGISTRY.pop(name, None)

def get(name):
    return REGISTRY.get(name)

def all_commands():
    return sorted(REGISTRY.keys())
PY

#################################################

echo "[2] bootstrap"

cat > python/ados/router/bootstrap.py <<'PY'
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
PY

echo
echo DONE
