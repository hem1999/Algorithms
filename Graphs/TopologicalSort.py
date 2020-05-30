from queue import Queue
from graph import *
from AdjacencyMatrixRepresentation import AdjacencyMatrix

def Topological_sort(graph):

    queue  = Queue()

    indegreeMap = {}

    for i in range(graph.numVertices):
         indegreeMap[i] = graph.get_indegree(i)

         if indegreeMap[i]==0:
             queue.put(i)
    sorted_list = []
    while not queue.empty():
        vertex = queue.get()

        sorted_list.append(vertex)

        for v in graph.get_adjacent_vertices(vertex):
            indegreeMap[v] = indegreeMap[v]-1

            if indegreeMap[v] == 0:
                queue.put(v)

    if len(sorted_list)!=graph.numVertices:
        raise ValueError("This graph has a circle")

    print(sorted_list)

if __name__=='__main__':
    g = AdjacencyMatrix(9,directed=True)
    g.add_edge(0,1)
    g.add_edge(1,2)
    g.add_edge(2,7)
    g.add_edge(2,4)
    g.add_edge(2,3)
    g.add_edge(1,5)
    g.add_edge(5,6)
    g.add_edge(3,6)
    g.add_edge(3,4)
    g.add_edge(6,8)
    Topological_sort(g)
