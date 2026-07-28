from ados.core.providers.local.qwen import QwenProvider


class ProviderRouter:

    def __init__(self):
        self.providers = [
            QwenProvider(),
        ]

    def select(self):

        for provider in self.providers:

            print(
                provider.name,
                provider.available()
            )

            if provider.available():
                return provider

        raise RuntimeError("No provider available")
