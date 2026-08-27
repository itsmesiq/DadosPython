arquivo = open('texto.txt', 'w')

texto = list()

texto.append('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
texto.append('Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
texto.append('Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.')

arquivo.write('\n'.join(texto))
arquivo.close()

print('Arquivo "texto.txt" criado com sucesso e conteúdo escrito.')