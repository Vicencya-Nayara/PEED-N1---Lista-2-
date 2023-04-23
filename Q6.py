#Crie uma lista vazia e peça para o usuário digitar 10 números. 
#Em seguida, adicione esses números à lista utilizando um loop for.

#Criando lista vazia
lista = []

for i in range(10):
    numeros = int(input('Digite um número: '))
    lista.append(numeros)

print('Lista: ', lista)
