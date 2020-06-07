import math
from AdjacencyMatrixRepresentation import AdjacencyMatrix
from queue import Queue
def dijkstras(graph,source,destination):

    distance_table = {}
    for i in range(graph.numVertices):
        distance_table[i] = (math.inf,None)
    distance_table[source] = (0,source)

    queue = Queue()
    queue.put(source)
    processed_nodes = []
    while len(processed_nodes)!=graph.numVertices:
        current_vertex = queue.get()
        if current_vertex not in processed_nodes:
            for i in current_vertex.get_adjacent_vertices():
                if distance_table[i][0] is None:
                    distance_table[i] = (graph.get_edge_weight(current_vertex,i),current_vertex)
                else:
                    if distance_table[current_vetex][0]+graph.get_edge_weight(current_vertex,i)<distance_table[i][0]:
                        distance_table[i] = (distance_table[current_vetex][0]+graph.get_edge_weight(current_vertex,i),current_vertex)
        preprocessed_nodes.append(current_vetex)
    return distance_table

if __name__=='__main__':
    g = AdjacencyMatrix(9,True)
    g.add_edge(0,1)
    g.add_edge(1,2)
    g.add_edge(2,7)
    g.add_edge(2,4)
    g.add_edge(2,3)
    g.add_edge(1,5)
    g.add_edge(5,6)
    g.add_edge(6,3)
    g.add_edge(3,4)
    g.add_edge(6,8)
    print(dijkstras(g,1,8))
