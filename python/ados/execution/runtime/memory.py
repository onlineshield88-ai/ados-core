class RuntimeMemory:

    def __init__(self):
        self._memory = {}

    def put(self, key, value):
        self._memory[key] = value

    def get(self, key, default=None):
        return self._memory.get(key, default)

    def delete(self, key):
        self._memory.pop(key, None)

    def clear(self):
        self._memory.clear()

    def keys(self):
        return list(self._memory.keys())

    def dump(self):
        return dict(self._memory)
