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
        return f"nome = {self.name} specie = {self.species}"

class Fence:
    def __init__(self, area: float, temperature: float, habitat: str) -> None:
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.lista_animali: list[Animal] = []

    def add(self, animal: Animal) -> None:
        self.lista_animali.append(animal)

    def __str__(self) -> str:
        repr: str = ""
        for animal in self.lista_animali:
            repr += animal.__str__() + "\n"
        return repr

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

lupo = Animal("giovanni","blb", 10, 5,5,"Continental")

lorenzo.add_animal(lupo,recinto)

print(recinto)