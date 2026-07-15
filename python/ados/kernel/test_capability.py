import ados.kernel.bootstrap

from pprint import pprint
from ados.kernel.capability import dump
from ados.kernel.capability import providers

print()

pprint(dump())

print()

print(
    providers("graph")

)
