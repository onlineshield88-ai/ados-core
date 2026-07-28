from abc import ABC, abstractmethod

class Module(ABC):

    name = "module"
    priority = 100

    @abstractmethod
    def supports(self, event):
        ...

    @abstractmethod
    def handle(self, event):
        ...
