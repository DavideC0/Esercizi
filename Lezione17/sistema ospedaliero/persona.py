class Persona:
    def __init__(self, nome: str, cognome: str) -> None:
        if type(nome) == str:
            self.__nome: str|None = nome
        else:
            self.__nome: str|None = None
            print("Il nome non è valido")
        if type(cognome) == str:
            self.__cognome: str|None = cognome
        else:
            self.__cognome: str|None = None
            print("Il cognome non è valido")
        if self.__nome and self.__cognome == None:
            self.__età: int|None = None
    
    def setNome(self, nome: str) -> None:
        if type(nome) == str:
            self.__nome: str|None = nome
        else:
            print("Il nome non è valido, non è stato possibile modificarlo")
            
    def setCognome(self, cognome: str) -> None:
        if type(cognome) == str:
            self.__cognome: str|None = cognome
        else:
            print("Il cognome non è valido, non è stato possibile modificarlo")
    
    def setEtà(self, età: int) -> None:
        if type(età) == int:
            self.__età: int|None = età
        else:
            print("L'età non è valida, non è stata possibile modificarla")
            
    def getNome(self) -> str:
        return self.__nome
    
    def getCognome(self) -> str:
        return self.__cognome

    def getEtà(self) -> int:
        return self.__età
    
    def greet(self) -> str:
        return f"Ciao, sono {self.__nome} {self.__cognome}! Ho {self.__età} anni!"