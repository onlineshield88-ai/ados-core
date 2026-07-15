from ados.kernel import bus


def hello(data):
    print("EVENT:", data)


bus.subscribe("demo", hello)

bus.publish(
    "demo",
    {
        "message": "ADOS Kernel Online"
    }
)
