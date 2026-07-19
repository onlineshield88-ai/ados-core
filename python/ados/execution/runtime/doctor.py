from ados.engine.loader import EngineLoader
from ados.knowledge.manager import Knowledge

def doctor():

    print("="*60)

    print("Registered Engines")

    for e in EngineLoader().load():
        print(" -",e)

    print()

    print("Knowledge")

    for k in Knowledge().folders():
        print(" -",k)

    print("="*60)
