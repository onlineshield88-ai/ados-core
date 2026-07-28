from ados.core.context.builder import ContextBuilder
from ados.core.providers.router import ProviderRouter
from ados.core.session.session import Session

class Kernel:

    def __init__(self):

        self.context=ContextBuilder()
        self.router=ProviderRouter()
        self.session=Session()

    def ask(self,prompt:str):

        self.session.append("user",prompt)

        ctx=self.context.build(prompt)

        provider=self.router.select()

        answer=provider.generate(ctx)

        self.session.append("assistant",answer)

        return answer
