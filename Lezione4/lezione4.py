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