class Reasoner:

    def next_step(self, objective, context):

        if not context.get("planned"):
            return "planner"

        if not context.get("knowledge"):
            return "knowledge"

        if not context.get("task"):
            return "executor"

        return "finish"
