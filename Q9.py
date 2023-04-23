#Peça para o usuário digitar 10 números e crie um conjunto com esses números. 
#Em seguida, remova todos os números pares do conjunto.

numeros = set()

for i in range(10):
    num = int(input('Digite um número: '))
    numeros.add(num)

remover_num = int(input('Digite o número que quer remover: '))
if remover_num in numeros:
    numeros.remove(remover_num)
    print('Número removido!', numeros)
else:
    print('\nNúmero não existe no conjunto.')