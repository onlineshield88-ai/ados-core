from ados.core.providers.router import ProviderRouter

router=ProviderRouter()

def run(prompt):

    provider=router.select()

    print(f"[Brain] Provider : {provider.name}")

    return provider.generate(prompt)
