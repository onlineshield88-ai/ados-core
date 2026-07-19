from ados.reasoning.agent import Agent
from ados.execution.task import Task


class PlannerAgent(Agent):

    name = "planner"

    def run(self, context):

        objective = context.get("objective", "Unnamed Objective")

        tasks = [
            Task(
                id="plan-001",
                title="Analyze Repository",
                priority=10,
            ),
            Task(
                id="plan-002",
                title="Load Knowledge",
                priority=9,
            ),
            Task(
                id="plan-003",
                title="Generate Execution Plan",
                priority=8,
            ),
        ]

        context["planned"] = True
        context["objective"] = objective
        context["tasks"] = tasks

        return context


agent = PlannerAgent()
