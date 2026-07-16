#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 8.1"
echo " Planner Engine"
echo "======================================"

mkdir -p \
python/ados/planner

echo "[1] planner"

cat > python/ados/planner/planner.py <<'PY'
class Planner:

    def plan(self, objective):

        return [
            {
                "id":1,
                "type":"analysis",
                "goal":objective
            }
        ]
PY

touch python/ados/planner/__init__.py

echo "[2] cli"

cat > python/ados/cli/planner.py <<'PY'
from ados.planner.planner import Planner


def run(args=None):

    if args is None or len(args)==0:

        print("planner <objective>")
        return

    p=Planner()

    tasks=p.plan(" ".join(args))

    for t in tasks:

        print(t)
PY

echo
echo DONE
