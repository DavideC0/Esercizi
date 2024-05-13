class Animal:
    def __init__(self, age, name) -> None:
        self.age = age
        self.name = name

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"
    
    def talk(self):
        return "Non sa parlare..."

class Person(Animal):
    
    def talk(self):
        return f"Ciao mi chiamo {self.name}"
    
    def __add__(self, other):
        return Person(name=self.name + other.name, age=self.age + other.age)
    
class Student(Person):
    
    def __init__(self, age, name, id) -> None:
        super().__init__(age, name)
        self.id = id
    
    def talk(self):
        return f"Ciao io sono uno studente e mi chiamo {self.name}"
    
    def __str__(self) -> str:
        return super().__str__() + f" id = {self.id}"
    
a = Animal(name="bardh", age=28)
print(a.talk())
p = Person(name="Walter", age=38)
print(p)
print(p.talk())
s = Student(name="Crhistian", age=26, id=1234)
print(s)
print(s.talk())

p2 = Person(40, "gionno")

p3 = p + p2
print(p3)