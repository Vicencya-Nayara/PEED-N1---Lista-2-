#Crie uma lista vazia e peça para o usuário digitar 10 números. Em seguida, retorne os elementos de índice par da lista.

lista = []

for i in range(10):
    numeros = int(input('Digite um número: '))
    lista.append(numeros)

for numero in lista:
    if numero % 2 == 0:
        print(numero, end=' ')