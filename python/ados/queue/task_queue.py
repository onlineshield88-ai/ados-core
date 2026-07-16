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
