#Peça para o usuário digitar 5 números e crie uma tupla com esses números. 
#Em seguida, retorne o primeiro elemento da tupla.

#Iniciando com a tupla vazia
tupla = ()

for i in range(5):
    numero = int(input('Digite um número: '))
    tupla.append(numero)

tupla_numeros = tuple(numero)
print('O primeiro elemento da tupla é:', tupla_numeros[0])