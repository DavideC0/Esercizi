from abc import ABC, abstractmethod
from math import ceil

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
        metà = ceil(len(testoInChiaro)/2)
        
    
    def decodifica(self, testoCodificato: str) -> str:
        return super().decodifica(testoCodificato)        
        
c = CifratoreAScorrimento(5000)

pippo = c.codifica("Ciao, come stai?")
oppip = c.decodifica(pippo)
print(pippo)
print(oppip)