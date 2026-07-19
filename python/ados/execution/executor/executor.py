class Executor:

    def __init__(self):
        self.handlers = {}

    def register(self, task_type, handler):
        self.handlers[task_type] = handler

    def execute(self, task):

        handler = self.handlers.get(task.metadata.get("type"))

        if handler is None:
            print("No executor:", task.metadata.get("type"))
            return

        return handler(task)

    def list(self):
        return sorted(self.handlers.keys())
