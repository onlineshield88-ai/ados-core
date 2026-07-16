class Reflector:

    def evaluate(self, task, result):

        report = {
            "task": task.title,
            "success": True,
            "result": result,
            "next_action": "continue"
        }

        if result is None:
            report["success"] = False
            report["next_action"] = "retry"

        return report
