#9-1 Restaurant
class Restaurant:
    def __init__(self, nome: str, tipo_cucina: str) -> None:
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.numb_served: int = 0

    def open_restaurant(self) -> str:
        return "Il ristorante è aperto"
    
    def describe_restaurant(self) -> str:
        return f"Nome = {self.nome} tipo di cucina = {self.tipo_cucina}"
    
    def set_numb_served(self, num: int):
        self.numb_served = num
    
    def increment_number_served(self) -> None:
        self.numb_served += 1

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
        self.tentativi_login: int = 0
    
    def describe_user(self) -> str:
        return f"nome = {self.nome} cognome = {self.cognome} residenza = {self.residenza} età = {self.età}"
    
    def greet_user(self) -> str:
        return f"benvenuto {self.cognome} {self.nome}, cosa desideri fare?"
    
    def increment_login_attemps(self) -> None:
        self.tentativi_login += 1

    def reset_login_attempts(self) -> None:
        self.tentativi_login = 0

davide = Users("Davide", "Calcagni", "Roma", 19)
maffo = Users("Andrea", "Maffei", "Castel Giubileo", 20)
print(davide.describe_user())
print(davide.greet_user())
print(maffo.describe_user())
print(maffo.greet_user())

#9-4 Number Served
print(ristorante.numb_served)
ristorante.set_numb_served(5)
print(ristorante.numb_served)
for i in range(5):
    ristorante.increment_number_served()
print(ristorante.numb_served)

#9-5 Login Attempts
print(maffo.tentativi_login)
for i in range(5):
    maffo.increment_login_attemps()
print(maffo.tentativi_login)
maffo.reset_login_attempts()
print(maffo.tentativi_login)

#9-6 Ice Cream Stand
class IceCreamStand(Restaurant):
    def __init__(self, nome: str, tipo_cucina: str, sapori: list[str]) -> None:
        self.sapori: list[str] = sapori
        super().__init__(nome, tipo_cucina)

    def display_flavors(self):
        repr: str = ""
        for i in range(len(self.sapori)):
            repr += self.sapori[i] + "\n"
        return repr
    
gelateria = IceCreamStand("o' scampia o' vesuvio", "gelateria", ["ciccolato", "fior di latte", "nocciola"])
print(gelateria.display_flavors())