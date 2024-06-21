from abc import ABC

class Forma(ABC):
    def getArea(self):
        pass
    
    def render(self):
        pass

class Quadrato(Forma):
    def __init__(self, lato: int) -> None:
        self.lato: int = lato
        
    def getArea(self):
        return self.lato * self.lato
    
    def render(self):
        render: str = "*" * self.lato + "\n"
        for _ in range(self.lato - 2):
            render += "*" + " " * (self.lato - 2) + "*\n"
        render += "*" * self.lato
        return render

class Rettangolo(Forma):
    def __init__(self, base: int, altezza: int) -> None:
        self.base: int = base
        self.altezza: int = altezza
    
    def getArea(self):
        return self.base * self.altezza
    
    def render(self):
        render: str = "*" * self.base + "\n"
        for _ in range(self.altezza - 2):
            render += "*" + " " * (self.base - 2) + "*\n"
        render += "*" * self.base
        return render
        
quadrato: Quadrato = Quadrato(4)
print(quadrato.render())
rettangolo: Rettangolo = Rettangolo(base = 8, altezza = 4)
print(rettangolo.render())