#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 9.3"
echo " Reasoning Engine"
echo "======================================"

mkdir -p \
python/ados/reasoning

echo "[1] reasoning"

cat > python/ados/reasoning/__init__.py <<'PY'
from .reasoner import Reasoner
PY

cat > python/ados/reasoning/reasoner.py <<'PY'
class Reasoner:

    def next_step(self, objective, context):

        if not context.get("planned"):
            return "planner"

        if not context.get("knowledge"):
            return "knowledge"

        if not context.get("task"):
            return "executor"

        return "finish"
PY

echo "[2] init"

echo
echo DONE
