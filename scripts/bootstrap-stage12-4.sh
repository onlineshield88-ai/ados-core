#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 12.4"
echo " Agent Router"
echo "======================================"

mkdir -p python/ados/router

cat > python/ados/router/router.py <<'PY'
class AgentRouter:

    def __init__(self):
        self.routes = {}

    def register(self, task_type, agent_name):
        self.routes[task_type] = agent_name

    def resolve(self, task):

        t = task.metadata.get("type")

        return self.routes.get(t)
PY

cat > python/ados/router/__init__.py <<'PY'
from .router import AgentRouter
PY

echo
echo "[1] router"
echo "[2] exports"

echo
echo DONE
