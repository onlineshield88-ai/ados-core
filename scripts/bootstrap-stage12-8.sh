#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 12.8"
echo " Autonomous Runtime Loop"
echo "======================================"

mkdir -p python/ados/runtime

cat > python/ados/runtime/loop.py <<'PY'
class RuntimeLoop:

    def __init__(self,
                 queue,
                 dispatcher,
                 reflector):

        self.queue = queue
        self.dispatcher = dispatcher
        self.reflector = reflector

    def run(self, context):

        completed = []

        while not self.queue.empty():

            task = self.queue.pop()

            self.dispatcher.dispatch(
                task,
                context
            )

            task.status = "completed"

            report = self.reflector.evaluate(
                task,
                task.status
            )

            completed.append(report)

        return completed
PY

cat >> python/ados/runtime/__init__.py <<'PY'

from .loop import RuntimeLoop
PY

echo
echo "[1] runtime loop"
echo "[2] exports"

echo
echo DONE
