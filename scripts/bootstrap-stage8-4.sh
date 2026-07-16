#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 8.4"
echo " Universal Task Model"
echo "======================================"

mkdir -p \
python/ados/task

echo "[1] task"

cat > python/ados/task/task.py <<'PY'
from dataclasses import dataclass, field


@dataclass
class Task:

    id: str
    title: str

    description: str = ""

    status: str = "pending"

    priority: int = 0

    depends_on: list = field(default_factory=list)

    metadata: dict = field(default_factory=dict)
PY

echo "[2] init"

cat > python/ados/task/__init__.py <<'PY'
from .task import Task
PY

echo
echo DONE
