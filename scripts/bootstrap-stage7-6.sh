#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 7.6"
echo " Event Bus Kernel"
echo "======================================"

mkdir -p python/ados/kernel

########################################

echo "[1] event bus"

cat > python/ados/kernel/event_bus.py <<'PY'
class EventBus:

    def __init__(self):
        self._listeners = {}

    def subscribe(self, event, handler):

        self._listeners.setdefault(event, [])
        self._listeners[event].append(handler)

    def publish(self, event, payload=None):

        listeners = self._listeners.get(event, [])

        for fn in listeners:
            fn(payload)


bus = EventBus()
PY

########################################

echo "[2] init"

cat > python/ados/kernel/__init__.py <<'PY'
from .event_bus import bus
PY

echo
echo DONE
