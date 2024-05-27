import random

def mov_tartaruga(pos: list[str]) -> list[str]:
    r: int = random.randint(1,100)
    if r <= 50:
        indice: int = pos.index('T') + 3
        if indice >= len(pos):
            pos[pos.index('T')] = '-'
            pos[-1] = 'T'
        else:
            pos[pos.index('T')] = '-'
            pos[indice] = 'T'
    elif 50 < r <= 70:
        indice: int = pos.index('T') - 6
        if indice < 0:
            pos[pos.index('T')] = '-'
            pos[0] = 'T'
        else:
            pos[pos.index('T')] = '-'
            pos[indice] = 'T'
    elif r > 70:
        indice: int = pos.index('T') + 1
        if indice >= len(pos):
            pos[pos.index('T')] = '-'
            pos[-1] = 'T'
        else:
            pos[pos.index('T')] = '-'
            pos[indice] = 'T'
    return pos

def mov_lepre(pos: list[str]) -> list[str]:
    r: int = random.randint(1,100)
    if r <= 20:
        return pos
    elif 20 < r <= 40:
        indice: int = pos.index('L') + 9
        if indice >= len(pos):
            pos[pos.index('L')] = '-'
            pos[-1] = 'L'
        else:
            pos[pos.index('L')] = '-'
            pos[indice] = 'L'
    elif 40 < r <= 50:
        indice: int = pos.index('L') - 12
        if indice < 0:
            pos[pos.index('L')] = '-'
            pos[0] = 'L'
        else:
            pos[pos.index('L')] = '-'
            pos[indice] = 'L'
    elif 50 < r <= 80:
        indice: int = pos.index('L') + 1
        if indice >= len(pos):
            pos[pos.index('L')] = '-'
            pos[-1] = 'L'
        else:
            pos[pos.index('L')] = '-'
            pos[indice] = 'L'
    elif r > 80:
        indice: int = pos.index('L') - 1
        if indice < 0:
            pos[pos.index('L')] = '-'
            pos[0] = 'L'
        else:
            pos[pos.index('L')] = '-'
            pos[indice] = 'L'
    return pos

def visualizza(pos_tartaruga: list[str], pos_lepre: list[str]) -> None:
    pass

pos_tartaruga: list[str] = ['-' for i in range(71)]
pos_lepre: list[str] = pos_tartaruga.copy()
pos_tartaruga[0] = 'T'
pos_lepre[0] = 'L'

while True:
    pos_tartaruga = mov_tartaruga(pos_tartaruga)
    if pos_tartaruga[-1] == 'T':
        print('Vince la tartaruga')
        break
    pos_lepre = mov_lepre(pos_lepre)
    if pos_lepre[-1] == 'L':
        print('Vince la lepre')
        break
    