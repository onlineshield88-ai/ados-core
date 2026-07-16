class ToolRegistry:

    def __init__(self):
        self.tools = {}

    def register(self, name, tool):
        self.tools[name] = tool

    def unregister(self, name):
        self.tools.pop(name, None)

    def get(self, name):
        return self.tools.get(name)

    def list(self):
        return sorted(self.tools.keys())
