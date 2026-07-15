CAPABILITIES = {}


def register(name, capability):

    CAPABILITIES.setdefault(name, set())
    CAPABILITIES[name].add(capability)


def unregister(name):

    CAPABILITIES.pop(name, None)


def get(name):

    return sorted(CAPABILITIES.get(name, []))


def providers(capability):

    result = []

    for provider, caps in CAPABILITIES.items():

        if capability in caps:
            result.append(provider)

    return sorted(result)


def dump():

    return {
        k: sorted(v)
        for k, v in CAPABILITIES.items()
    }
