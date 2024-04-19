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

def rewrite_dict(d: dict[str,int], somma: int) -> dict[str, int]:
    d1: dict = d.copy()    
    for key in d1:
        d1[key] = d1[key] / somma
    
    return d1

d: dict = {"ciao": 2, "hello": 3}
d1: dict = rewrite_dict(d,crea_somma(d))
print(f"Il dizionario normale è {d}, quello trasformato è {d1}")