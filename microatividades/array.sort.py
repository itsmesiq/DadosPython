import random

numeros = [random.randint(1,100) for _ in range(15)]

print('Array original:', numeros)

numeros.sort()
print('Array ordenado crescente:', numeros)

numeros.sort(key=None, reverse=True)
print('Array ordenado decrescente:', numeros)

dados = ['nome', 'dataNascimento', 'cpf', 'rg']

print('Array de String original:', dados)

dados.sort()
print('Array de String ordenado crescente:', dados)

dados.sort(key=None, reverse=True)
print('Array de String ordenado decrescente:', dados)