from abc import ABC, abstractmethod

class CodificatoreMessaggio(ABC):
    @abstractmethod
    def codifica(self, testoInChiaro: str) -> str:
        pass

class DecodificatoreMessaggio(ABC):
    @abstractmethod
    def decodifica(self, testoCodificato: str) -> str:
        pass

class CifratoreAScorrimento(CodificatoreMessaggio,DecodificatoreMessaggio):
    def __init__(self, chiave: int) -> None:
        self.chiave = chiave
        
    def codifica(self, testoInChiaro: str):
        codificato = ""
        for c in testoInChiaro:
            if c != " ":
                num_unicode = ord(c) + self.chiave
                codificato += chr(num_unicode)
            else:
                codificato += " "
        return codificato

    def decodifica(self, testoCodificato: str) -> str:
        decodificato = ""
        for c in testoCodificato:
            if c != " ":
                num_unicode = ord(c) - self.chiave
                decodificato += chr(num_unicode)
            else:
                decodificato += " "
        return decodificato
    
class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, chiave: int) -> None:
        self.chiave = chiave
    
    def codifica(self, testoInChiaro: str) -> str:
        codificato = self.apoggio(testoInChiaro)
        print(codificato)
        for _ in range(self.chiave):
            codificato = self.apoggio(codificato)
            print(codificato)
        return codificato
    
    def apoggio(self, codifica):
        metà = len(codifica)//2
        codificato = ""
        for i in range(metà):
            codificato += codifica[i] + codifica[metà + i]
        return codificato
    
    def decodifica(self, testoCodificato: str) -> str:
        metà = len(testoCodificato//2)
        decodificato = ""      
        
c = CifratoreAScorrimento(4000)

"""pippo = c.codifica("Ciao, come stai?")
oppip = c.decodifica(pippo)
print(pippo)
print(oppip)"""

walter = CifratoreACombinazione(3)
gianno = walter.codifica("Ciao, come stai?")
