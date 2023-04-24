#Crie um grafo vazio. Peça para o usuário digitar os vértices e as arestas desse grafo. 
#O usuário deve informar os pares de vértices que formam cada aresta. Em seguida, verifique se a aresta ('A', 'C') está presente no grafo.

grafo = {}

num_vertice = int(input('Digite o número de vertice do grafo'))
for i in  range(num_vertice):
    vertice = input('Digite o nome do vértice: ')
    grafo[vertice] = []

num_aresta = int(input('Digite o número de arestas: '))
for i in range(num_aresta):
    origem, destino = input('Digite os vértices que formam as arestas: ')
    grafo[origem].append(destino)
    grafo[destino].append(origem)

print(grafo)

if 'A' in grafo and 'C' in grafo['A']:
    print("A aresta ('A', 'C') está presente no grafo")
else:
    print("A aresta ('A', 'C') não está presente no grafo")