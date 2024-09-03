import random

def bubble_sort(x: list):
    for _ in range(len(x)):
        for j in range(len(x) - 1):
            if x[j] > x[j + 1]:
                temp: int = x[j]
                x[j] = x[j + 1]
                x[j + 1] = temp
                
def genera_lista() -> list[int]:
    lista: list = []
    for _ in range(8):
        lista.append(random.randint(0, 10000))
    return lista

l: list = genera_lista()
print(l)
l = bubble_sort(l)
print(l)    