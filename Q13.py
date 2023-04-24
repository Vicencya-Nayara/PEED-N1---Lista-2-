#Crie um dicionário vazio. Peça para o usuário digitar as chaves e os valores desse dicionário. 
#Em seguida, verifique se a chave 'profissão' está presente no dicionário.

dicionario = {}

chave = input('Digite uma chave: ')
valor = input('Digite um valor: ')

dicionario[chave] = valor

if 'profissão'or 'Profissão' in dicionario:
    print('A palavra Profisão apareceu no dicionário')
else:
    print('A palavra profissão não foi encontrada no dicionário')