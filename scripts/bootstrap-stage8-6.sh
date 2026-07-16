#!/data/data/com.termux/files/usr/bin/bash

echo "======================================"
echo " ADOS STAGE 8.6"
echo " Workflow Engine"
echo "======================================"

mkdir -p python/ados/workflow

cat > python/ados/workflow/__init__.py <<'EOF'
from .workflow import Workflow
EOF

cat > python/ados/workflow/workflow.py <<'EOF'
class Workflow:

    def __init__(self):
        self.steps=[]

    def add(self,step):
        self.steps.append(step)

    def run(self,context):

        for step in self.steps:
            step(context)

        return context
EOF

echo "[1] workflow"
echo "[2] init"

echo
echo DONE
