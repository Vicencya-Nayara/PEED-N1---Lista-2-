#Peça para o usuário digitar 5 números e crie uma lista com esses números. 
#Em seguida, peça para o usuário digitar mais um número e adicione esse número à lista.

lista = []

for i in range(0,5):
    numero = int(input('Digite um número:'))
    lista.append(numero)

novo_numero = int(input('\nDigite um novo número: '))
lista.append(novo_numero)

print('Lista de números: ', lista)

