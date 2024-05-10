class Animal:
    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str) -> None:
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health: float = 100 * (1/self.age)
    
    def calcolo_area(self):
        return self.height * self.width
    
    def __str__(self) -> str:
        return (f"Name: {self.name} "
                f"Species: {self.species} "
                f"Age: {self.age} "
                f"Height: {self.height} "
                f"Width: {self.width} "
                f"Preferred Habitat: {self.preferred_habitat} "
                f"Health: {self.health}")


class Fence:
    def __init__(self, area: float, temperature: float, habitat: str) -> None:
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.lista_animali: list[Animal] = []

    def add(self, animal: Animal) -> None:
        self.lista_animali.append(animal)
        self.area -= animal.calcolo_area()

    def __str__(self) -> str:
        repr: str = ""
        for animal in self.lista_animali:
            repr += animal.__str__() + "\n"
        repr += f"area = {self.area} temperatura = {self.temperature} habitat = {self.habitat}"
        return repr
    
    def print_area(self) -> str:
        return self.area

class ZooKeeper: 
    def __init__(self, nome: str, cognome: str, id: int) -> None: 
        self.nome = nome
        self.cognome = cognome
        self.id = id
    
    def add_animal(self, animal: Animal, fence: Fence):
        if animal.preferred_habitat == fence.habitat and fence.area >= animal.calcolo_area():
            if animal not in fence.lista_animali:
                fence.add(animal)

class Zoo:
    def __init__(self) -> None:
        self.lista_recinti: list[Fence] = []
        self.lista_guardiani: list[ZooKeeper] = []

lorenzo = ZooKeeper("Lorenzo", "Maggi", 1234)

recinto = Fence(100,25,"Continental")
recinto_vuoto = Fence(100,25,"dinosauri")

print(recinto)

lupo = Animal("giovanni","blb", 10, 5, 5,"Continental")
cavallo = Animal('pietro','palle', 20, 10, 5, 'Continental')
gatto = Animal('adrian','savona', 20, 10, 10, 'dinosauri')
cane = Animal('nicola','ltimat-piderma', 20, 25, 1, 'Continental')

lorenzo.add_animal(lupo,recinto)
print(f"recinto 1 {recinto.print_area()}") #75 primo
lorenzo.add_animal(cavallo,recinto)
print(f"recinto 1 {recinto.print_area()}") #25 primo
lorenzo.add_animal(gatto,recinto)
print(f"recinto 1 {recinto.print_area()}") #25 non entra primo
lorenzo.add_animal(cane,recinto)
print(f"recinto 1 {recinto.print_area()}") #0 primo
print(f"recinto 2 {recinto_vuoto.print_area()}") #100 secondo
lorenzo.add_animal(gatto,recinto_vuoto)
print(f"recinto 2 {recinto_vuoto.print_area()}") #0 secondo
lorenzo.add_animal(lupo,recinto_vuoto)
print(f"recinto 2 {recinto_vuoto.print_area()}") #0 non entra secondo