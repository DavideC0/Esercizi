import math

class Media:
    def __init__(self, titolo: str) -> None:
        self.titolo: str = titolo
        self.valutazione: list[int] = []
        
    def set_title(self, titolo: str):
        pass
    
    def get_title(self) -> str:
        pass
    
    def set_rating(self, valutazione: int):
        pass
    
    def get_rating(self) -> int:
        pass

    def get_media(self) -> float:
        pass
    
    def get_rate(self) -> str:
        pass
    
class Film(Media):
    def __init__(self, titolo: str, durata: int) -> None:
        super().__init__(titolo)
        self.durata: int = durata
        
    def set_title(self, titolo: str):
        self.titolo = titolo
        
    def get_title(self) -> str:
        return self.titolo
    
    def set_rating(self, valutazione: int):
        if 0 < valutazione <= 5:
            self.valutazione.append(valutazione)
        else:
            print("Errore")
    
    def get_rating(self) -> int:
        return self.valutazione
    
    def get_media(self) -> float:
        return sum(self.valutazione) / len(self.valutazione)
    
    def get_rate(self) -> str:
        media = math.ceil(self.get_media())
        if media == 1:
            return f"Terribile"
        elif media == 2:
            return f"Brutto"
        elif media == 3:
            return f"Normale"
        elif media == 4:
            return f"Bello"
        elif media == 5:
            return f"Grandioso"
    