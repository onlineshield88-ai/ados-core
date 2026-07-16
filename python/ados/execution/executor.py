class TaskExecutor:

    def __init__(self, queue):

        self.queue = queue

    def run(self, callback):

        results = []

        while not self.queue.empty():

            task = self.queue.pop()

            results.append(callback(task))

        return results
