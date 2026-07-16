class DependencyResolver:

    def __init__(self, graph):
        self.graph = graph
        self.completed = set()

    def complete(self, task_id):
        self.completed.add(task_id)

    def ready(self):

        ready = []

        for task in self.graph.tasks():

            if task.id in self.completed:
                continue

            deps = task.depends_on

            if all(d in self.completed for d in deps):
                ready.append(task)

        return ready
