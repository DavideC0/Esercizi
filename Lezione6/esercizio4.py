class Food:
    def __init__(self, name: str, price: float) -> None:
        self.name: str = name
        self.price: float = price
    
    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price
    
    def __str__(self) -> str:
        return f"nome = {self.name} prezzo = {self.price}"
    
class Menu:
    def __init__(self) -> None:
        self.list_food: list[Food] = []

    def add_food(self, food):
        self.list_food.append(food)
    
    def remove_food(self, food) -> None:
        if food in self.list_food:
            self.list_food.remove(food)
    
    def get_prices(self):
        list_price: list = []
        for i in range(len(self.list_food)):
            list_price.append(self.list_food[i].get_price())
        return list_price
    
    def get_avg_price(self):
        return sum(self.get_prices()) / len(self.list_food)

pizza = Food("Pizza", 10)
pasta = Food("Pasta", 7.90)
zuppa = Food("Zuppa", 20.50)

menu = Menu()

menu.add_food(pizza)
menu.add_food(pasta)
menu.add_food(zuppa)

print(f"Lista prezzi: {menu.get_prices()}")
print(f"Media dei prezzi: {menu.get_avg_price()}")