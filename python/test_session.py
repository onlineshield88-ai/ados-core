from ados.core.session.session import Session

s=Session()

s.append("user","hello")

s.append("assistant","hi")

print(s.load())
