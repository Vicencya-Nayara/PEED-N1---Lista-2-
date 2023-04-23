#Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes. 
#Em seguida, verifique quantas vezes o nome 'Maria' aparece na tupla.

nomes = tuple(input('Digite 3 nomes: ').split(','))

#count serve para saber a quantidade de vezes que o nome aparece
quantidade_maria = nomes.count('Maria')
print('A quantidade de vezes que o nome Maria aparece é:', quantidade_maria, end='.')
