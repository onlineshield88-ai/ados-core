from ados.execution.execution import TaskExecutor


class ExecutionEngine:

    def __init__(self, queue):

        self.executor = TaskExecutor(queue)

    def execute(self):

        results = []

        def worker(task):

            task.status = "completed"

            results.append(task)

            return task

        self.executor.run(worker)

        return results
