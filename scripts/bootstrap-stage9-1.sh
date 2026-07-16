#!/data/data/com.termux/files/usr/bin/bash

echo "======================================"
echo " ADOS STAGE 9.1"
echo " Objective Engine"
echo "======================================"

mkdir -p python/ados/objective

echo "[1] objective"

cat > python/ados/objective/objective.py <<'PY'
from dataclasses import dataclass


@dataclass
class Objective:

    goal: str

    priority: int = 1

    metadata: dict = None

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}
PY

echo "[2] init"

cat > python/ados/objective/__init__.py <<'PY'
from .objective import Objective
PY

echo
echo DONE
