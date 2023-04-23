#Crie um dicionário vazio. Peça para o usuário digitar as chaves e os valores desse dicionário. 
#Em seguida, retorne o valor da chave 'idade'.

dicionario = {}

#Pedindo ao usuário para digitar as chaves e valores do dicionário
for i in range(3):
    chave = input('Digite a chave: ')
    valor = input('Digite o valor: ')
    dicionario[chave] = valor

#Retornando o valor da chave 'idade' se ela existir no dicionário
if 'idade' in dicionario:
    print('O valor da chave idade é: ', dicionario['idade'])
else:
    print('O valor idade não foi encontrado.')