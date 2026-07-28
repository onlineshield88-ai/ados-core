from ados.core.providers.base import Provider
from ados.core.runtime.llama_runtime import LlamaRuntime

class QwenProvider(Provider):

    name="qwen"

    priority=99

    def __init__(self):
        self.runtime=LlamaRuntime()

    def available(self):
        return self.runtime.health()

    def generate(self,prompt):
        return self.runtime.generate(prompt)
