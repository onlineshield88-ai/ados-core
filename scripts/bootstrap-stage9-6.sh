#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 9.6"
echo " Reflection Engine"
echo "======================================"

mkdir -p python/ados/reflection

echo "[1] reflection"

cat > python/ados/reflection/__init__.py <<'PY'
from .reflector import Reflector
PY

cat > python/ados/reflection/reflector.py <<'PY'
class Reflector:

    def evaluate(self, task, result):

        report = {
            "task": task.title,
            "success": True,
            "result": result,
            "next_action": "continue"
        }

        if result is None:
            report["success"] = False
            report["next_action"] = "retry"

        return report
PY

echo "[2] init"

echo
echo DONE
