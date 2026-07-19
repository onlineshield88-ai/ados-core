from collections import defaultdict


class EventBus:

    def __init__(self):
        self._events = defaultdict(list)

    def subscribe(self, event, handler):
        self._events[event].append(handler)

    def publish(self, event, payload=None):

        for handler in self._events.get(event, []):
            handler(payload)

    def listeners(self, event=None):

        if event is None:
            return dict(self._events)

        return self._events.get(event, [])
