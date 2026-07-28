class Registry:

    def __init__(self):
        self.modules = []

    def register(self, module):
        self.modules.append(module)
        self.modules.sort(key=lambda m: m.priority)

    def get_modules(self):
        return self.modules
