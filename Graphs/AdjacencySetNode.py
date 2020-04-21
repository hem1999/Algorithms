class Node:

    def __init__(self,vertexId):
        self.vertexId = vertexId
        self.adjacency_set = set()

    def add_edge(self,v):
        if self.vertexId == v:
            raise ValueError("An vertex cannot be adjacent to itself")
        self.adjacency_set.add(v)

    def get_adjacency_vertices(self):
        return sorted(self.adjacency_set)
