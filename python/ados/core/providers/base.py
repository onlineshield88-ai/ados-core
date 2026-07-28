from abc import ABC, abstractmethod

class Provider(ABC):

    name="provider"

    priority=100

    @abstractmethod
    def available(self):
        pass

    @abstractmethod
    def generate(self,prompt):
        pass
