#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 10.1"
echo " Runtime Context"
echo "======================================"

mkdir -p \
python/ados/runtime

echo "[1] context"

cat > python/ados/runtime/context.py <<'PY'
from dataclasses import dataclass, field


@dataclass
class RuntimeContext:

    objective = None

    tasks: list = field(default_factory=list)

    knowledge: dict = field(default_factory=dict)

    memory: dict = field(default_factory=dict)

    reflection: dict = field(default_factory=dict)

    state: dict = field(default_factory=dict)
PY

echo "[2] init"

cat > python/ados/runtime/__init__.py <<'PY'
from .doctor import doctor
from .context import RuntimeContext
PY

echo
echo DONE
