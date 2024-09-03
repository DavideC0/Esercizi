from abc import ABC, abstractclassmethod
from typing import Any

class abcAnimal(ABC):
    
    @abstractclassmethod
    def verso(self):
        pass

class Cane(abcAnimal):
    def __init__(self, nome:str) -> None:
        self.nome:str = nome
        
    def verso(sefl):
        print(f"Bau!")
        
class Gatto(abcAnimal):
    def __init__(self, nome:str) -> None:
        self.nome:str = nome
        
    def verso(sefl):
        print(f"Miao!")
        
class Coccodrillo(abcAnimal):
    def __init__(self, nome:str) -> None:
        self.nome:str = nome
        
    def verso(self):
        print(f"roar?")

a: dict[str,str|int] = {'key1': 'val1', 'key2': 'val2', 'key3': 3}

cane1:Cane = Cane('pluto')
gatto1:Gatto = Gatto('silvestro')
Coccodrillo1:Coccodrillo = Coccodrillo('Giovanni')

cane1.verso()
gatto1.verso()
Coccodrillo1.verso()