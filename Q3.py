#Crie um dicionário vazio. Peça para o usuário digitar uma chave e um valor e adicione esses dados ao dicionário. 
#Em seguida, peça para o usuário adicionar mais uma chave e um valor e adicione esses dados ao dicionário também.

# Criando um dicionário vazio
dicionario = {}

chave_1 = input('Digite uma chave: ')
valor_1 = input('Digite um valor: ')

# Adicionando a primeira chave e valor ao dicionáriO
dicionario[chave_1] = valor_1
print(dicionario)

chave_2 = input('Digite uma chave: ')
valor_2 = input('Digite um valor: ')
dicionario[chave_2] = valor_2
print(dicionario)