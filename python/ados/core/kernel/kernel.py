from ados.core.kernel.registry import Registry

class Kernel:

    def __init__(self):
        self.registry = Registry()

    def register(self, module):
        self.registry.register(module)

    def dispatch(self, event):

        for module in self.registry.get_modules():

            if module.supports(event):
                event = module.handle(event)

        return event
