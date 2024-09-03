import os

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
    
    def writeToFile(self, directory: str) -> None:
        with open(directory, "a") as appender:
            appender.write(self.getText())

class File(Documento):
    def __init__(self, testo: str, nomePercorso: str) -> None:
        super().__init__(testo)
        self.nome_percorso: str = nomePercorso
        if not os.path.isdir(nomePercorso):
            self.createDirectory(nomePercorso)
        else:
            print('Directory already exits')

    def createDirectory(self, nomePercorso: str):
        os.mkdir(nomePercorso)
        self.createFile(nomePercorso)

    def createFile(self, nomePercorso: str) -> str:
        with open(f"{nomePercorso}/document.txt", "a") as reader:
            testo = "Questo e' il contenuto del file: \n"
            reader.write(testo)
            reader.write(self.testo)
        return "document.txt"
    
    def leggiTestoDaFile(self) -> str:
        with open(f"{self.nome_percorso}/document.txt")  as reader:
            file = reader.read()
        return file
    

giorgio: File = File("Ciao Giorgio, come stai?", "esempiomdycr4f")
print(giorgio.leggiTestoDaFile( ))