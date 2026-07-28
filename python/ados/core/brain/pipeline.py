class Pipeline:

    def __init__(self):
        self.steps=[]

    def add(self,step):
        self.steps.append(step)

    def execute(self,data):

        result=data

        for step in self.steps:
            result=step(result)

        return result
