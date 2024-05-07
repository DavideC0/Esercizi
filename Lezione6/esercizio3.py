class Animal:
    def __init__(self, nome, tipo) -> None:
        self.nome = nome 
        self.tipo = tipo
        self.legs = None
    
    def set_legs(self, legs):
        self.legs = legs
    
    def get_legs(self):
        return self.legs
    
    def __str__(self) -> str:
        if self.legs:
            return f"Nome = {self.nome}, alimentazione = {self.tipo}, numero di gambe/zampe = {self.legs}"
        else:
            return f"Nome = {self.nome}, alimentazione = {self.tipo}"
        
gatto = Animal("gatto", "carivoro")
zebra = Animal("zebra", "erbivoro")

print(gatto)
print(zebra)

gatto.set_legs(4)
zebra.set_legs(8)

print(gatto)
print(zebra.get_legs())