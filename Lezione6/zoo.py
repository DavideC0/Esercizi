class Animal:
    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str) -> None:
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health: float = 100 * (1/self.age)
        self.recinto: Fence|None = None
    
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
        self.area_tot = area

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
        """
        consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. 
        L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat 
        e se c'è ancora spazio nel recinto, 
        ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.
        """
        if animal.preferred_habitat == fence.habitat and fence.area >= animal.calcolo_area():
            if animal not in fence.lista_animali:
                fence.add(animal)
                animal.recinto = fence
    
    def remove_animal(self, animal: Animal, fence: Fence):
        """
        consente al guardiano dello zoo di rimuovere un animale dallo zoo. L'animale deve essere allontanato dal suo recinto. 
        Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.
        """
        if animal in fence.lista_animali:
            fence.lista_animali.remove(animal)
            fence.area += animal.calcolo_area()
    
    def feed(self, animal: Animal):
        """
        implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli animali dello zoo. 
        Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, 
        ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. 
        Perciò, l'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.
        """
        height_maggiore: float = animal.height * (2/100) + animal.height
        width_maggiore: float = animal.width * (2/100) + animal.width
        area_maggiore: float = height_maggiore * width_maggiore
        area_differenza: float = area_maggiore - animal.calcolo_area()
        if area_differenza <= animal.recinto.area:
            animal.height = height_maggiore
            animal.width = width_maggiore
            animal.health = animal.health * (1/100) + animal.health
    
    def clean(self, fence: Fence) -> float:
        """
         implementare un metodo che consenta al guardiano dello zoo di pulire tutti i recinti dello zoo. 
         Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. 
         Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. 
         Se l'area residua è pari a 0, restituire l'area occupata.
        """
        if fence.area == 0:
            return fence.area_tot
        time: float = (fence.area_tot - fence.area) / fence.area
        
        

class Zoo:
    def __init__(self) -> None:
        self.lista_recinti: list[Fence] = []
        self.lista_guardiani: list[ZooKeeper] = []

lorenzo = ZooKeeper("Lorenzo", "Maggi", 1234)

recinto = Fence(100,25,"Continental")
recinto_vuoto = Fence(100,25,"dinosauri")

lupo = Animal("giovanni","blb", 10, 5, 5,"Continental")
cavallo = Animal('pietro','palle', 20, 10, 5, 'Continental')
gatto = Animal('adrian','savona', 20, 10, 10, 'dinosauri')
cane = Animal('nicola','ltimat-piderma', 20, 25, 1, 'Continental')
#test add
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

#test remove
lorenzo.remove_animal(lupo,recinto) #rimuove il lupo dal recinto
print(recinto)
lorenzo.remove_animal(cane,recinto_vuoto) #tenta di rimuovere il cane ma non funziona perchè fa parte del recinto
print(recinto) #ristampa ciò che è nel recinto è uguale 
print(recinto_vuoto) #stampa ciò che è nel secondo recito e non cambia

#test feed
print(lupo)# pre time skip
lorenzo.feed(lupo)# aggiunge massa
print(lupo) #post time skip
lorenzo.add_animal(lupo,recinto)#prova ad aggiungerlo ma fallisce
print(recinto)#controlla se l'aggiunge