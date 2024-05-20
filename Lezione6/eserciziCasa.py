#9-1 Restaurant
class Restaurant:
    def __init__(self, nome: str, tipo_cucina: str) -> None:
        self.nome = nome
        self.tipo_cucina = tipo_cucina

    def open_restaurant(self) -> str:
        return "Il ristorante è aperto"
    
    def describe_restaurant(self) -> str:
        return f"Nome = {self.nome} tipo di cucina = {self.tipo_cucina}"
ristorante = Restaurant("la primavera di vladimiro", "pizzeria")
print(f"Nome: {ristorante.nome} tipo di cucina: {ristorante.tipo_cucina}")
print(ristorante.open_restaurant())
print(ristorante.describe_restaurant())

#9-3 Users
class Users:
    def __init__(self, nome: str, cognome: str, residenza: str, età: int) -> None:
        self.nome = nome
        self.cognome = cognome
        self.residenza = residenza
        self.età = età
    
    def describe_user(self) -> str:
        return f"nome = {self.nome} cognome = {self.cognome} residenza = {self.residenza} età = {self.età}"
    
    def greet_user(self) -> str:
        return f"benvenuto {self.cognome} {self.nome}, cosa desideri fare?"
davide = Users("Davide", "Calcagni", "Roma", 19)
maffo = Users("Andrea", "Maffei", "Castel Giubileo", 20)
print(davide.describe_user())
print(davide.greet_user())
print(maffo.describe_user())
print(maffo.greet_user())