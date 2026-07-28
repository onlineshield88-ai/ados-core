from ados.core.providers.router import ProviderRouter

router=ProviderRouter()

provider=router.select()

print("Provider :",provider.name)

print(provider.generate("Say hello in one sentence"))
