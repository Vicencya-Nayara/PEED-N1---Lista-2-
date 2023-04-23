#Crie um grafo vazio. Peça para o usuário digitar os vértices e as arestas desse grafo. 
#O usuário deve informar os pares de vértices que formam cada aresta.

grafo = {}

num_vertice = int(input('Digite o número de vértices do grafo: '))
for i in range(num_vertice):
    vertice = input('Digite o nome do vértice:')
    grafo[vertice] = []

num_aresta = int(input('Digite o números de arestas: '))
for i in range(num_aresta):
    a, b = input('Digite os vertices que formam as arestas: ')
    grafo[a].append(b)
    grafo[b].append(a)

print(grafo)