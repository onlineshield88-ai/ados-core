class ServiceContainer:

    def __init__(self):
        self.services = {}

    def register(self, name, service):
        self.services[name] = service

    def unregister(self, name):
        self.services.pop(name, None)

    def get(self, name):
        return self.services.get(name)

    def has(self, name):
        return name in self.services

    def list(self):
        return sorted(self.services.keys())
