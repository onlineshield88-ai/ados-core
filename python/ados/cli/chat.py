from ados.core.brain.brain import ADOSBrain

def main():

    brain=ADOSBrain()

    print()
    print("============================")
    print(" ADOS Development OS")
    print("============================")

    while True:

        try:
            prompt=input("\nYou > ")
        except KeyboardInterrupt:
            print()
            break

        if prompt.lower() in ("exit","quit"):
            break

        print()
        print(brain.ask(prompt))
