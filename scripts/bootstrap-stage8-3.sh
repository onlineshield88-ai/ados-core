#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 8.3"
echo " Kernel Service Container"
echo "======================================"

mkdir -p python/ados/kernel

echo "[1] service container"

cat > python/ados/kernel/container.py <<'PY'
class ServiceContainer:

    def __init__(self):
        self.services = {}

    def register(self, name, service):
        self.services[name] = service

    def unregister(self, name):
        self.services.pop(name, None)

    def get(self, name):
        return self.services.get(name)

    def has(self, name):
        return name in self.services

    def list(self):
        return sorted(self.services.keys())
PY

echo "[2] init"

cat > python/ados/kernel/__init__.py <<'PY'
from .container import ServiceContainer
PY

echo
echo DONE
