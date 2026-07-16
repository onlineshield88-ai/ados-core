#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 11.7"
echo " Agent Pipeline"
echo "======================================"

mkdir -p python/ados/pipeline

cat > python/ados/pipeline/pipeline.py <<'PY'
class AgentPipeline:

    def __init__(self, manager):
        self.manager = manager
        self.steps = []

    def add(self, agent):

        self.steps.append(agent)

    def run(self, context):

        for step in self.steps:
            self.manager.run(step, context)

        return context
PY

cat > python/ados/pipeline/__init__.py <<'PY'
from .pipeline import AgentPipeline
PY

echo
echo "[1] pipeline"
echo "[2] exports"

echo
echo DONE
