def sequenza(numero: int):
    if numero <= 2:
        return 1
    else:
        return sequenza(numero-1) + sequenza(numero-2)

def fibonacci(numero: int):
    memoria = [0,1]
    for i in range(1, numero):
        risultato = memoria[i-1] + memoria[i]
        memoria.append(risultato)
    return memoria

n=10
print(sequenza(n))

print(fibonacci(100))