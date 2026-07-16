#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 12.0"
echo " Task Queue"
echo "======================================"

mkdir -p python/ados/queue

cat > python/ados/queue/task_queue.py <<'PY'
from collections import deque


class TaskQueue:

    def __init__(self):
        self._queue = deque()

    def push(self, task):
        self._queue.append(task)

    def pop(self):
        if self._queue:
            return self._queue.popleft()
        return None

    def pending(self):
        return len(self._queue)

    def empty(self):
        return len(self._queue) == 0

    def list(self):
        return list(self._queue)
PY

cat > python/ados/queue/__init__.py <<'PY'
from .task_queue import TaskQueue
PY

echo
echo "[1] task queue"
echo "[2] exports"

echo
echo DONE
