from AdjacencySetNode import Node
from graph import Graph
class AdjacencySet(Graph):

    def __init__(self,numVertices,directed=False):
        super(AdjacencySetRepresentation,self).__init__(numVertices,directed)
        self.vertex_list = []
        for i in range(numVertices):
            self.vertex_list.append(Node(i))

    def add_edge(self,v1,v2,weight=1):
        if v1 >= self.numVertices or v2>= self.numVertices or v1<0 or v2<0:
            raise ValueError("Vertices out of bounds")

        self.vertex_list[v1].add_edge(v2)
        if not self.directed:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacenct_vertices(self,v):
        return self.vertex_list[v].get_adjacency_vertices()


    def get_indegree(self,v):
        if v<0 or v>=self.numVertices:
            raise ValueError("Cannot access the vertex")
        indegree=0
        for i in range(self.numVertices):
            if v in self.get_adjancent_vertices(i):
                indegree+=1
        return indegree

    def get_edge_weight(self,v1,v2):
        return "Method not yet ready"

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacency_vertices(i):
                print(i,"-->",v)
