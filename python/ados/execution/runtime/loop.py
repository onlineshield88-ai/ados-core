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
