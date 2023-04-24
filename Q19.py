#Peça para o usuário digitar 5 números e crie um conjunto com esses números. Em seguida, verifique quantos elementos estão no conjunto.

conjunto = set()

for i in range(5):
    numeros = int(input('Digite um número: '))
    conjunto.add(numeros)

print('O conjunto de números é: ', conjunto)
print('O conjunto tem', len(conjunto), 'elemetos.')