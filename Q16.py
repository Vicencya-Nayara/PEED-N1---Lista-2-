#Peça para o usuário digitar 10 números e crie uma lista com esses números. 
#Em seguida, multiplique cada elemento da lista por 2 e crie uma nova lista com esses valores.

lista = []

for i in range(10):
    numeros = int(input('Digite um número: '))
    lista.append(numeros)

print(lista)

mult = []
for i in lista:
    mult.append(i * 2)

print(mult)