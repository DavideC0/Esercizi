from persona import Persona

class Paziente(Persona):
    def __init__(self, nome: str, cognome: str, id: str) -> None:
        super().__init__(nome, cognome)
        self.__id: str = id
        
    def setId(self, id: str) -> None:
        self.__id = id
    
    def getId(self) -> str:
        return self.__id
    
    def infoPaziente(self) -> None:
        print(f"{self.greet()} ID: {self.getId()}")