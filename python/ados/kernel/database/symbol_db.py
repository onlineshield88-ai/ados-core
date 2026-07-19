class SymbolDatabase:

    def __init__(self):
        self._symbols = []

    def load(self, symbols):
        self._symbols = list(symbols)

    def all(self):
        return list(self._symbols)

    def find_type(self, symbol_type):
        return [
            s for s in self._symbols
            if s["type"] == symbol_type
        ]

    def find_name(self, name):
        return [
            s for s in self._symbols
            if name.lower() in s["name"].lower()
        ]

    def count(self):
        return len(self._symbols)
