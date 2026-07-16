#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 10.2"
echo " Runtime Session"
echo "======================================"

mkdir -p python/ados/runtime

cat > python/ados/runtime/session.py <<'PY'
from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class RuntimeSession:

    id: str = field(default_factory=lambda: str(uuid4()))

    user: str = "local"

    project: str = ""

    state: dict = field(default_factory=dict)
PY

cat > python/ados/runtime/__init__.py <<'PY'
from .doctor import doctor
from .context import RuntimeContext
from .session import RuntimeSession
PY

echo
echo "[1] runtime session"
echo "[2] exports"
echo
echo "DONE"
