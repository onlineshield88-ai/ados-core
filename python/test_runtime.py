from ados.core.runtime.llama_runtime import LlamaRuntime

llm=LlamaRuntime()

print("Health :",llm.health())

print()

print(llm.generate("Say hello in one sentence."))
