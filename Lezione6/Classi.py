class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hobby = []

    def set_hobby(self, new_hobby):
        self.hobby.append(new_hobby)
    
    def remove_hobby(self, old_hobby):
        if old_hobby in self.hobby:
            self.hobby.remove(old_hobby)

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)
davide = Person("Davide C.", 19)
walter = Person("Walter P.", 25)
catalina = Person("Catalina T.", 21)

print(f"Età di {bob.name}: {bob.age}")

lista_persone: list = [alice, bob, davide, walter]

giovane: Person = lista_persone[0]

for persona in range(len(lista_persone)):
    if giovane.age > lista_persone[persona].age:
        giovane = lista_persone[persona]

print(f"la persona più giovane è {giovane.name} ed ha età {giovane.age} anni")