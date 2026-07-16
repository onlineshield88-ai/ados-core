class Orchestrator:

    def __init__(self):
        self.services = {}

    def register(self, name, service):
        self.services[name] = service

    def get(self, name):
        return self.services.get(name)

    def run(self, objective):
        print("Objective :", objective.goal)
        print("Registered Services :", sorted(self.services.keys()))
