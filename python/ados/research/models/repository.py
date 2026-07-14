from dataclasses import dataclass

@dataclass
class Repository:

    name:str

    full_name:str=""

    description:str=""

    language:str=""

    stars:int=0

    forks:int=0

    license:str=""

    topics:list=None
