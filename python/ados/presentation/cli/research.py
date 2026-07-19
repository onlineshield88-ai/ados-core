import sys

def run(args=None):

    if args is None:
        args=[]

    if len(args)==0:
        print("research commands:")
        print(" scan <url>")
        print(" extract")
        print(" graph")
        print(" compare")
        print(" features")
        return

    cmd=args[0]

    if cmd=="scan":
        print("scan repository")

    elif cmd=="extract":
        print("extract knowledge")

    elif cmd=="graph":
        print("build graph")

    elif cmd=="compare":
        print("compare repositories")

    elif cmd=="features":
        print("detect features")

    else:
        print("Unknown research command")
