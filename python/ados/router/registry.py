REGISTRY = {}

def register(name, handler):
    REGISTRY[name] = handler

def unregister(name):
    REGISTRY.pop(name, None)

def get(name):
    return REGISTRY.get(name)

def all_commands():
    return sorted(REGISTRY.keys())
