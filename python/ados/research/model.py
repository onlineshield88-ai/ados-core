from dataclasses import dataclass

@dataclass
class Repository:

    name:str
    url:str

    language:str=""
    stars:int=0

    architecture:int=0
    cli:int=0
    plugins:int=0
    memory:int=0
    testing:int=0
    docs:int=0

    total:int=0
