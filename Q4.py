#Peça para o usuário digitar 5 números e crie um conjunto com esses números.
#Em seguida, peça para o usuário escolher um dos números e removê-lo do conjunto

#Criando um cojunto. Usa-se SET() para criar
numeros = set()
for i in range(0,5):
    numero = int(input('Digite um número: '))
    numeros.add(numero)

#Mostrando o conjunto
print('\nConjunto Original: ', numeros)

#Pedindo para remover do conjunto
numero_remover = int(input('Digite o número que deseja remover: '))
if numero_remover in numeros:
    numeros.remove(numero_remover)
    print('Numero removido! Conjunto atualizado: ', numeros)
else:
    print('O número digitado não está no conjunto!')

