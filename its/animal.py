from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, age: int):
        super().__init__()
        self.name = name
        self.age = age
        
    @abstractmethod
    def make_sound(self):
        pass
    
class Cat(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        
    def make_sound(self):
        print("Miao!")

class Dog(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        
    def make_sound(self):
        print("Bau!")