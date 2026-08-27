import random

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


numeros = [random.randint(1,100) for _ in range(15)]

print('Array original:', numeros)

bubbleSort(numeros)

print('Array ordenado crescente:', numeros)