#Crie um grafo vazio. Peça para o usuário digitar os vértices e as arestas desse grafo. 
#O usuário deve informar os pares de vértices que formam cada aresta.Em seguida, peça para o usuário escolher uma das arestas e removê-la do grafo

grafo = {}

num_vertice = int(input('Digite o número de vértices do grafo: '))
for i in range(num_vertice):
    vertice = input('Digite o nome do vértice:')
    grafo[vertice] = []

num_aresta = int(input('Digite o números de arestas: '))
for i in range(num_aresta):
    origem, destino = input('Digite os vertices que formam as arestas: ').split()
    grafo[origem].append(destino)
    grafo[destino].append(origem)

print(grafo)

# Remover uma aresta
o , d = input('Digite os vértices que formam a aresta a ser removida: ').split()
if d in grafo and o in grafo:
    grafo[o].remove(d)
    grafo[d].remove(o)

print(grafo)
