from persona import Persona

class Dottore(Persona):
    def __init__(self, nome: str, cognome: str, specializzazione: str, parcella: float) -> None:
        super().__init__(nome, cognome)
        if type(specializzazione) == str:
            self.__specializzazione: str|None = specializzazione
        else:
            self.__specializzazione: str|None = None
            print("La specializzazione inserita non è valida")
        
        if type(parcella) == float:
            self.__parcella: float|None = parcella
        else:
            self.__parcella: float|None = None
            print("Il valore della parcella deve essere float")
            
    def setSpecializzazione(self, specializzazione: str) -> None:
        if type(specializzazione) == str:
            self.__specializzazione: str|None = specializzazione
        else:
            print("La specializzazione inserita non è valida, il valore non è stato aggiornato")
            
    def setParcella(self, parcella: float) -> None:
        if type(parcella) == float:
            self.__parcella = parcella
        else:
            print("Il valore della parcella deve essere float, il valore non è stato aggiornato")
    
    def getSpecializzazione(self) -> str:
        return self.__specializzazione
    
    def getParcella(self) -> float:
        return self.__parcella
    
    def isValid(self) -> bool:
        if self.getEtà() >= 30:
            print(f"Il dottore {self.getNome()} {self.getCognome()} ha più di 30 anni quindi è valido")
            return True
        else:
            print(f"Il dottore {self.getNome()} {self.getCognome()} ha meno di 30 anni quindi non è valido")
            return False
            
    def doctorGreet(self) -> None:
        print(f"{self.greet()} Sono un medico {self.__specializzazione}")