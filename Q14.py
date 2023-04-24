#Peça para o usuário digitar 5 números e crie um conjunto com esses números. Em seguida, verifique se o número 3 está presente no conjunto

conjunto = set()

for i in range(5):
    numeros = int(input('Digite um número: '))
    conjunto.add(numeros)

print(conjunto)

if 3 in conjunto:
    print('O número 3 está no conjunto.')
else:
    print('O número 3 não faz parte do conjunto.')