class AgentRegistry:

    def __init__(self):
        self._agents={}

    def register(self,name,agent):
        self._agents[name]=agent

    def get(self,name):
        return self._agents.get(name)

    def list(self):
        return sorted(self._agents.keys())
