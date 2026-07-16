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
