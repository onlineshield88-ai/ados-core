from ados.core.brain.pipeline import Pipeline

from ados.core.brain.stages.load_context import run as context

from ados.core.brain.stages.planner import run as planner

from ados.core.brain.stages.provider import run as provider

from ados.core.brain.stages.review import run as review

class ADOSBrain:

    def __init__(self):

        self.pipeline=Pipeline()

        self.pipeline.add(context)

        self.pipeline.add(planner)

        self.pipeline.add(provider)

        self.pipeline.add(review)

    def ask(self,prompt):

        return self.pipeline.execute(prompt)
