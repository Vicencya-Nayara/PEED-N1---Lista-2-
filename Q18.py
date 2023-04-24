#Crie um dicionário vazio. Peça para o usuário digitar as chaves e os valores desse dicionário. 
#Em seguida, adicione uma nova chave e valor ao dicionário, onde a chave é 'cidade' e o valor é a cidade em que o usuário nasceu.

dicionario = {}

# solicita as chaves e valores do dicionário
while True:
    chave = input('Digite uma chave: ')
    if chave == 'fim':
        break
    valor = input('Digite um valor: ')
    dicionario[chave] = valor

# adiciona uma nova chave e valor ao dicionário
cidade_nascimento = input('Digite em qual cidade você nasceu: ')
dicionario['cidade'] = cidade_nascimento

print(dicionario)