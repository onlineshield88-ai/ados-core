#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 10.5"
echo " Runtime Scheduler"
echo "======================================"

mkdir -p python/ados/runtime

cat > python/ados/runtime/scheduler.py <<'PY'
from collections import deque


class RuntimeScheduler:

    def __init__(self):
        self.queue = deque()

    def schedule(self, task):
        self.queue.append(task)

    def next(self):
        if not self.queue:
            return None
        return self.queue.popleft()

    def pending(self):
        return len(self.queue)

    def clear(self):
        self.queue.clear()
PY

cat > python/ados/runtime/__init__.py <<'PY'
from .doctor import doctor
from .context import RuntimeContext
from .session import RuntimeSession
from .memory import RuntimeMemory
from .events import EventBus
from .scheduler import RuntimeScheduler
PY

echo
echo "[1] runtime scheduler"
echo "[2] exports"

echo
echo "DONE"
