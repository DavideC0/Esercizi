#4-1
pizza: list = ["margherita", "diavola", "marinara"]
for i in range(len(pizza)):
    print(f"Il tipo di pizza che preferisco è: {pizza[i]}")

#4-2
animali: list = ["gatto", "cane", "coniglio"]
for i in range(len(animali)):
    print(f"Il {animali[i]} è un ottimo animale")

#4-3
print("Numeri da 1 a 20 incluso")
for i in range(1, 21):
    print(i)

#4-4
one_milion: list = []
for i in range(10000001):
    one_milion.append(i)
print("Stampare tutto impiegherebbe troppo tempo, non lo farò")

#4-5
massimo: int = max(one_milion)
minimo: int = min(one_milion)
somma: int = sum(one_milion)
print(f"Il massimo della lista è {massimo}, il minimo è {minimo} infine la somma di tutti gli eleenti è {somma}")

#4-6
print("Stampo solo i numeri dispari da 1 a 20")
for i in range(1, 21, 2):
 print(i)

 #4-7
 print("Stampo la tabelillina del 3")
 for i in range(3, 31, 3):
    print(i)

#4-8
print("Stampo i cubi da 1 a 10")
for i in range(1, 11):
   print(i**3)

#4-9
lista_10_cubi: list = [i**3 for i in range(1, 11)]
print(f"Stampo la lista dei cubi da 1 10 {lista_10_cubi}")

#4-10
lista_slice: list = []
middle: int = len(one_milion) // 2
middle_1: int = middle + 2
middle_2: int = middle - 1
lista_slice.extend(pizza[:3])
lista_slice.extend(one_milion[middle_2:middle_1])
lista_slice.extend(lista_10_cubi[-3:])
print(lista_slice)

#4-11
friend_pizza: list = pizza.copy()
pizza.append("patatine e wurstel")
friend_pizza.append("focaccia")
print("Le mie pizze preferite sono")
for i in range(len(pizza)):
   print(pizza[i])
print("Le pizze preferite dei miei amici sono")
for i in range(len(pizza)):
   print(friend_pizza[i])

#5-1
car: str = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')
print("Is car == 'audi'? I predict False")
print(car == 'audi')

#5-3
colore_alieno: str = "blu"
print("il colore è verde")
print(colore_alieno is "verde")
print("il colore è blu")
print(colore_alieno is "blu")