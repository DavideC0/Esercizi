from abc import ABC, abstractclassmethod

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


cane1 = Cane('pluto')
gatto1 = Gatto('silvestro')
Coccodrillo1 = Coccodrillo('Giovanni')

cane1.verso()
gatto1.verso()
Coccodrillo1.verso()