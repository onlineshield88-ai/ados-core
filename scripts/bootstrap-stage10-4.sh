#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 10.4"
echo " Runtime Event System"
echo "======================================"

mkdir -p python/ados/runtime

cat > python/ados/runtime/events.py <<'PY'
from collections import defaultdict


class EventBus:

    def __init__(self):
        self._events = defaultdict(list)

    def subscribe(self, event, handler):
        self._events[event].append(handler)

    def publish(self, event, payload=None):

        for handler in self._events.get(event, []):
            handler(payload)

    def listeners(self, event=None):

        if event is None:
            return dict(self._events)

        return self._events.get(event, [])
PY

cat > python/ados/runtime/__init__.py <<'PY'
from .doctor import doctor
from .context import RuntimeContext
from .session import RuntimeSession
from .memory import RuntimeMemory
from .events import EventBus
PY

echo
echo "[1] runtime event bus"
echo "[2] exports"

echo
echo "DONE"
