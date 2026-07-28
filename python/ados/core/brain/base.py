from abc import ABC, abstractmethod

class Brain(ABC):

    @abstractmethod
    def run(self, prompt: str):
        ...
