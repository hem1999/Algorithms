#In this code we are going to find the shortest path
#between two nodes in a unweighted graph using bfs

from AdjacencyMatrixRepresentation import AdjacencyMatrix
from queue import Queue
def bfs(g,start,end):

    prev = solve(g,start,end)
    print(prev)
    return reconstructPath(g,start,end,prev)

def solve(g,start,end):
    q = Queue()
    q.put(start)

    visited = [False for i in range(g.numVertices)]
    visited[start] = True

    prev = [None for i in range(g.numVertices)]

    while not q.empty():
        node = q.get()
        for i in g.get_adjacent_vertices(node):
            if not visited[i]:
                q.put(i)
                visited[i]=True
                prev[i]=node
    return prev

def reconstructPath(g,start,end,prev):
    path = []
    index = prev.index(end)
    for i in prev[:index+1][::-1]:
        path.add(i)

    path.reverse()
    if path[0]==start:
        return path
    return []

if __name__=='__main__':
    g = AdjacencyMatrix(6)
    g.add_edge(0,1)
    g.add_edge(0,3)
    g.add_edge(0,5)
    g.add_edge(1,2)
    g.add_edge(2,3)
    g.add_edge(3,4)
    g.add_edge(4,5)
    print(bfs(g,2,5))
