def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    dictionary: dict[str:list[int]] = {}
    for i in range(len(tuples)):
        if tuples[i][0] in dictionary:
            dictionary[tuples[i][0]].append(tuples[i][1])
        else:
            dictionary[tuples[i][0]] = [tuples[i][1]]
    return dictionary

