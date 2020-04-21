from AdjacencyMatrixRepresentation import AdjacencyMatrix
from AdjacencySetGraph import AdjacencySet
g = AdjacencyMatrix(4)

g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(2,3)

for i in range(4):
    print("Adjacent to: ",i,g.get_adjacent_vertices(i))

for i in range(4):
    print("indegree of ",i,g.get_indegree(i))

for i in range(4):
    for j in g.get_adjacent_vertices(i):
        print("Edge Weights of ",i," ",j," :",g.get_edge_weight(i,j))
print("++++++++++++++++++++++++++++++++++++++++++++")
print("Adjacency Set Representation: ")
g = AdjacencySet(4)

g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(2,3)

for i in range(4):
    print("Adjacent to: ",i,g.get_adjacent_vertices(i))

for i in range(4):
    print("indegree of ",i,g.get_indegree(i))

for i in range(4):
    for j in g.get_adjacent_vertices(i):
        print("Edge Weights of ",i," ",j," :",g.get_edge_weight(i,j))
