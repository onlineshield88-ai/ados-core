class EventBus:

    def __init__(self):
        self._listeners = {}

    def subscribe(self, event, handler):

        self._listeners.setdefault(event, [])
        self._listeners[event].append(handler)

    def publish(self, event, payload=None):

        listeners = self._listeners.get(event, [])

        for fn in listeners:
            fn(payload)


bus = EventBus()
