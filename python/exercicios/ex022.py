nome = str(input('Digite o seu nome: ')).strip()
nomeupper = nome.upper()
nomelower = nome.lower()
print('Nome em letras maiusculas: {}'.format(nomeupper))
print('Nome em letras minusculas: {}'.format(nomelower))
print('Quantidade de letras tem no nome: {}'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('O seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
