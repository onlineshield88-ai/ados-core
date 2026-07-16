from ados.planner.planner import Planner


def run(args=None):

    if args is None or len(args)==0:

        print("planner <objective>")
        return

    p=Planner()

    tasks=p.plan(" ".join(args))

    for t in tasks:

        print(t)
