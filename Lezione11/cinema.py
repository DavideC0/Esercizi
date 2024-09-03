class Film:
    def __init__(self, titolo: str, durata: float) -> None:
        self.titolo: str = titolo
        self.durata: float = durata
        
    def __str__(self) -> str:
        return f"Titolo = {self.titolo}, durata = {self.durata}"
    
class Sala:
    def __init__(self, id: str, posti_tot: int) -> None:
        self.id: str = id
        self.posti_tot: int = posti_tot
        self.programmazione: Film|None = None
        self.posti_prenotati: int = 0
        
    def prenota_posti(self, num_posti: int) -> bool:
        temp: int = num_posti + self.posti_prenotati
        if not(temp > self.posti_tot):
            self.posti_prenotati += num_posti
            return True
        return False
    
    def posti_disponibili(self) -> int:
        return self.posti_tot - self.posti_prenotati
    
class Cinema:
    def __init__(self) -> None:
        self.sale: list [Sala] = []
        
    def aggiungi_sala(self, sala: Sala) -> None:
        if sala not in self.sale:
            self.sale.append(sala)
            
    def prenota_film(self, titolo_film: str, num_post: int) -> bool:
        for i in self.sale:
            if i.programmazione.titolo == titolo_film:
                check: bool = i.prenota_posti(num_post)
                if check:
                    return f"Posti prenotati con successo"
                else:
                    return f"Errore, non ci sono abbastanza posti disponibili"
        return f"Errore, film non trovato"