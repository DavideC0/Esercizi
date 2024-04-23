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
for i in range(21):
    print(i)

#4-4
one_milion: list = []
for i in range(10000000):
    one_milion.append(i)
print("Stampare tutto impiegherebbe troppo tempo, non lo farò")