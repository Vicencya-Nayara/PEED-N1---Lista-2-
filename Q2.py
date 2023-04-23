#Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes. 
#Em seguida, peça para o usuário escolher um dos nomes e substituir esse nome por outro nome que ele também deve digitar.

#iniciando com tupla vazia
tupla = ()

#preenchendo no for
for i in range(0,3):
    nomes = input('Digite um nome: ')
    tupla += (nomes, )

#Mostrando a tupla original para os usuários
print('Os nomes digitados foram: ', tupla)

# Solicitando que o usuário escolha um nome para substituir e o novo nome
nome_antigo = input('\nQual nome deseja substituir: ')
novo_nome = input('Digite o novo nome:')

# Convertendo a tupla em uma lista para poder modificar o valor
lista_nomes = list(tupla)
if nome_antigo in lista_nomes:
    lista_nomes[lista_nomes.index(nome_antigo)] = novo_nome
    nomes_atualizados = tuple(lista_nomes)
    print('\nOs nomes atualizados são: ', nomes_atualizados)
else:
    print('O nome não foi encontrado na lista', tupla)