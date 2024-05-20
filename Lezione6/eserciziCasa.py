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