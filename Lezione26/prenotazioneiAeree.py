from abc import ABC, abstractmethod

class Volo(ABC):
    def __init__(self, codice: str, capacità: int) -> None:
        self.codice: str = codice
        self.capacità: int = capacità
        self.prenotazioni: int = 0
    
    @abstractmethod
    def prenota_posto(self):
        pass
    
    @abstractmethod
    def posti_disponibili(self):
        pass
    
class VoloCommerciale(Volo):
    def __init__(self, codice: str, capacità: int) -> None:
        super().__init__(codice, capacità)
        self.posti_economica: int = (self.capacità * 70) // 100
        self.posti_business: int = (self.capacità * 20 ) // 20
        self.posti_prima: int = self.capacità - self.posti_economica - self.posti_business
        self.prenotazioni_economica: int = 0
        self.prenotazioni_business: int = 0
        self.prenotazioni_prima: int = 0
    
    def prenota_posto(self, classe_servizio: str, posti: int):
        if classe_servizio == 'economica':
            if self.prenotazioni_economica + posti <= self.posti_economica:
                self.prenotazioni_economica += posti
                self.prenotazioni += posti
                return f"Sono stati prenotati {posti} nella classe economica, codice volo: {self.codice}"
            else:
                return f"Non ci sono abbastanza posti disponili"
        elif classe_servizio == 'business':
            if self.prenotazioni_business + posti <= self.posti_business:
                self.prenotazioni_business += posti
                self.prenotazioni += posti
                return f"Sono stati prenotati {posti} nella classe business, codice volo: {self.codice}"
            else:
                return f"Non ci sono abbastanza posti disponili"
        elif classe_servizio == 'prima':
            if self.prenotazioni_prima + posti <= self.posti_prima:
                self.prenotazioni_prima += posti
                self.prenotazioni += posti
                return f"Sono stati prenotati {posti} in prima classe, codice volo: {self.codice}"
            else:
                return f"Non ci sono abbastanza posti disponili"
        else:
            return f"Non esiste la classe scritta"
            
    def posti_disponibili(self):
        return {'posti disponibili': self.capacità - self.prenotazioni,
                'classe economica': self.posti_economica - self.prenotazioni_economica,
                'classe business': self.posti_business - self.prenotazioni_business,
                'prima classe': self.posti_prima - self.prenotazioni_prima
                }

class VoloCharter(Volo):
    def __init__(self, codice: str, capacità: int, costo: float) -> None:
        super().__init__(codice, capacità)
        self.costo: float = costo
    
    def prenota_posto(self):
        if self.prenotazioni == 0:
            self.prenotazioni = self.capacità
            return f"Prenotazione del volo charter con codice {self.codice} è andata a buon fine, il prezzo pagato è {self.costo}"
        else:
            return f"Il volo charter con codice {self.codice} è già stato prenotato"
    
    def posti_disponibili(self):
        return f"I posti disponibili sono {self.capacità-self.prenotazioni}"