def aggrega_voti(voti: list) -> dict[str:list[int]]:
    dizionario: dict[str:list[int]] = {}
    if len(voti) == 0:
        return []
    for i in range(len(voti)):
        tmp_nome = voti[i]['nome']
        tmp_voto = voti[i]['voto']
        if tmp_nome in dizionario:
            dizionario[tmp_nome].append(tmp_voto)
        else:
            dizionario[tmp_nome] = [tmp_voto]
    return dizionario

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))

def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    dizionario: dict = {}
    for key, value in prodotti.items():
        tmp = (prodotti[key] / 100) * 10
        if prodotti[key] > 20:
            dizionario[key] = prodotti[key] - tmp
    return dizionario

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    if len(lista) == 0:
        return lista
    counter = 0
    for key, value in da_rimuovere.items():
        for i in range(len(lista)):
            if lista[i] == key and value+1 != counter:
                lista[i] = None
                counter += 1
    l: list = []
    for i in range(len(lista)):
        if lista[i]:
            l.append(lista[i])
    return l

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 1}))