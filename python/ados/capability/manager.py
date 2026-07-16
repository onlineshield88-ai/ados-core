class CapabilityManager:

    def __init__(self):
        self.capabilities = {}

    def register(self, name, handler):
        self.capabilities[name] = handler

    def unregister(self, name):
        self.capabilities.pop(name, None)

    def get(self, name):
        return self.capabilities.get(name)

    def list(self):
        return sorted(self.capabilities.keys())
