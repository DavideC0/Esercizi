def minDistance(word1: str, word2: str) -> int:
    operations: int = 0
    word1 = list(word1)
    word3 = list(word2)
    word2 = list(word2)
    for elem in word1:
        if elem not in word2:
            word1.remove(elem)
            if elem in word2:
                word2.remove(elem)
            operations += 1
        else:
            pass
    for elem in word2:
        if elem not in word1:
            word1.append(elem)
            operations +=1
    for i in range(len(word3)):
        if word3[i] != word1[i]:
            var = word1[i]
            word1[i] = word3[i]
            word1[i+1] = var
            operations += 1
    return operations, word1

print(minDistance('intention', 'execution'))