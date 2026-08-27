import time

palavras = list()

with open('texto.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        palavras.extend(linha.split()) 

python_sort = palavras.copy()
inicio = time.time()
python_sort.sort()
fim = time.time()
tempo_python = fim - inicio

print('Python Sort:', python_sort)
print('Tempo:', tempo_python, 'segundos')

with open('texto_ordenado.txt', 'w', encoding='utf-8') as arquivo_ordenado:
    arquivo_ordenado.write('\n'.join(python_sort))
    print('Arquivo "texto_ordenado.txt" criado com sucesso e conteúdo escrito.')