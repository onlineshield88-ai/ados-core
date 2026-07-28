from abc import ABC, abstractmethod

class Runtime(ABC):

    name = "runtime"

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass

    @abstractmethod
    def health(self) -> bool:
        pass
