from ados.knowledge.graph import TaskGraph
from ados.queue import TaskQueue
from ados.resolver import DependencyResolver
from ados.execution import ExecutionEngine


class RuntimeIntegration:

    def __init__(self):

        self.graph = TaskGraph()

        self.queue = TaskQueue()

    def load_tasks(self, tasks):

        for task in tasks:
            self.graph.add_task(task)

        resolver = DependencyResolver(self.graph)

        while True:

            ready = resolver.ready()

            if not ready:
                break

            for task in ready:

                self.queue.push(task)

                resolver.complete(task.id)

    def execute(self):

        engine = ExecutionEngine(self.queue)

        return engine.execute()
