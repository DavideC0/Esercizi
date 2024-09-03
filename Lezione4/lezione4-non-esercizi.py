"""
    Questa funzione prende in input un dizionario
    (e.s. d = {"ciao": 2, "hello": 3}) e restituisce
    un nuovo dizionario fatto così:
    d1 = {"ciao": 2/5, "hello": 3/5}) dove 5 è l somma
    dei valori di d, ossia 2 + 3 = 5

"""
def crea_somma(d: dict[str, int]) -> int:
    somma: int = 0
    for key in d:
        somma += d[key]
    return somma

def rewrite_dict(d: dict[str,int], somma: int) -> dict[str, float]:
    d1: dict = d.copy()    
    for key in d1:
        d1[key] = d1[key] / somma
    
    return d1

def subtract(x: float, y: float) -> float:
    s: float = x - y
    return s

def mediana(lista: list):
    lunghezza: int = len(lista)
    lista.sort()
    if lunghezza % 2 == 0: #in caso la lista è pari
        lunghezza //= 2
        print(lunghezza)
        media: float = (lista[lunghezza] + lista[lunghezza-1]) / 2
        return media
    else: #in caso sia la lista è dispari
        lunghezza //= 2
        print(lunghezza)
        media: float = lista[lunghezza]
        return media
    
def differenza_cumulativa(lista: list) -> float:
    differenza: float = lista[0]
    for i in range(len(lista)-1):
        differenza -= lista[i+1]
    return differenza

def differenza_cumulativa_index(lista: list, index: int) -> float:
    if -len(lista) <= index < len(lista):
        lista1: list = lista.copy()
        fulcro: int = lista1.pop(index)
        for i in range(len(lista1)):
            fulcro -= lista1[i]
        return fulcro
    else:
        print("L'indice inserito non è valido")

def subtract_all(lista: list, y: float) -> list:
    differenza: list = []
    for i in range(len(lista)):
        differenza.append(lista[i] - y)
    return differenza

def subtract_list_to_list(lista1: list, lista2: list) -> list:
    lista1_fun: list = lista1.copy()
    lista2_fun: list = lista2.copy()
    lista_risultato: list = []
    if len(lista1_fun) == len(lista2_fun):
        for i in range(len(lista1_fun)):
            lista_risultato.append(lista1_fun[i] - lista2_fun[i])
    elif len(lista1_fun) > len(lista2_fun):
        for i in range(len(lista2_fun)):
            lista_risultato.append(lista1_fun[i] - lista2_fun[i])
    else: 
        for i in range(len(lista1_fun)):
            lista_risultato.append(lista1_fun[i] - lista2_fun[i])
        
    return lista_risultato

d: dict = {"ciao": 2, "hello": 3}
d1: dict = rewrite_dict(d,crea_somma(d))
print(f"Il dizionario normale è {d}, quello trasformato è {d1}")
x, y = 10.4, 5.8
sottrazione: float = subtract(x,y)
print(f"La sottrazione tra {x} e {y} è {sottrazione}")

lista_pari:    list = [2,9,0,-1,25,2,4,3]
lista_dispari: list = [2,9,0,-1,25,2,4]

mediana_pari: float = mediana(lista_pari)
mediana_dispari: float = mediana(lista_dispari)

print(f"La mediana della lista pari ordinata è {mediana_pari}, invece la mediana della lista dispari ordinata è {mediana_dispari}")

lista_differenza: list = [1,2,3,4,5,6]

differenza: float = differenza_cumulativa(lista_differenza)
print(f"La differenza comulativa di della lista {lista_differenza} è {differenza}")
index: int = 3
differenza_index: float = differenza_cumulativa_index(lista_differenza, index)
print(f"La differenza cumulativa indice scelto della lista {lista_differenza} è {differenza_index}")

lista_differenza_sub: list = [1,2,3,4,5,6]
sub: float = 4

differenza_sub: list = subtract_all(lista_differenza_sub, sub)
print(f"La sottrazione sulla lista {lista_differenza} con il sottratore {sub} è {differenza_sub}")

l1: list = [1,2,3,4,8]
l2: list = [2,3,4,5,6 ]
output: list = subtract_list_to_list(l1,l2)
print(f"Il risultato della sottrazione della lista {l1} e la lista {l2} è {output}")