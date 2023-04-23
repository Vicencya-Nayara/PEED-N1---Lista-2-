#Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes. 
#Em seguida, verifique se o nome 'Maria' está presente na tupla.

nomes = tuple(input('Digite 3 nomes: ').split(','))

if 'Maria' in nomes:
    print('Maria está na tupla.')
else:
    print('Maria não está na tupla')



