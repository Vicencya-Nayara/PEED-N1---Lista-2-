#Peça para o usuário digitar 5 números e crie uma tupla com esses números. 
#Em seguida, retorne o primeiro elemento da tupla.

numeros = []

for i in range(5):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

tupla_numeros = tuple(numeros)
print('O primeiro elemento da tupla é:', tupla_numeros[0])
