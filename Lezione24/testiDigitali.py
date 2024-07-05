class Documento:
    def __init__(self, testo: str) -> None:
        self.testo: str = testo
    
    def getText(self) -> str:
        return self.testo
    
    def setText(self, testo: str) -> None:
        self.testo = testo
    
    def isInText(self, parola: str) -> bool:
        if parola in self.testo:
            return True
        return False
    
class Email(Documento):
    def __init__(self, testo: str, mittente: str, destinatario: str, titolo: str) -> None:
        super().__init__(testo)
        self.mittente: str = mittente
        self.destinatario: str = destinatario
        self.titolo: str = titolo
    
    def get_mittente(self) -> str:
        return self.mittente

    def set_mittente(self, mittente: str) -> None:
        self.mittente = mittente

    def get_destinatario(self) -> str:
        return self.destinatario

    def set_destinatario(self, destinatario: str) -> None:
        self.destinatario = destinatario

    def get_titolo(self) -> str:
        return self.titolo

    def set_titolo(self, titolo: str) -> None:
        self.titolo = titolo
        
    def getText(self) -> str:
        return f"Da: {self.get_mittente()} A: {self.get_destinatario()}\nTitolo: {self.get_titolo()}\nMessaggio: {super().getText()}"
    