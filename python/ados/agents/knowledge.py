from ados.agent import Agent


class KnowledgeAgent(Agent):

    name = "knowledge"

    def run(self, context):

        tasks = context.get("tasks", [])

        context["knowledge"] = {
            "task_count": len(tasks),
            "titles": [
                t.title
                for t in tasks
            ]
        }

        return context


agent = KnowledgeAgent()
