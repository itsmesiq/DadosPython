import random

numeros = [random.randint(1, 100) for _ in range(15)]

print('Array original:', numeros)

for i in range(len(numeros)):
    menor = i

    for j in range(i + 1, len(numeros)):
        if numeros[menor] > numeros[j]:
            menor = j

    numeros[i], numeros[menor] = numeros[menor], numeros[i]

print('Array ordenado:', numeros)
