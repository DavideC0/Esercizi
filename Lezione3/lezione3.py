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
for i in range(1, 10):
   print(i**3)