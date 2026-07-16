from ados.agent import Agent


class PlannerAgent(Agent):

    name = "planner"

    def run(self, context):

        context["planned"] = True

        return context


agent = PlannerAgent()
