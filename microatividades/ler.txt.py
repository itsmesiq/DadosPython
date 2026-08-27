arquivo = open("loremipsum.txt", "r")
conteudo = arquivo.read()

print('CONTEÚDO COMPLETO:')
print(conteudo)

arquivo.seek(0)  # Retorna o cursor para o início do arquivo
primeira_linha = arquivo.readline()
print('PRIMEIRA LINHA:')
print(primeira_linha)

arquivo.seek(0)
tres_primeiros = arquivo.read(3)
print('TRÊS PRIMEIROS CARACTERES:')
print(tres_primeiros)

arquivo.close()

with open('loremipsum.txt', 'r') as arquivo:
    conteudo = arquivo.read()

    print('CONTEÚDO COMPLETO (USANDO WITH):')
    print(conteudo)