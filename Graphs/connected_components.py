from AdjacencyMatrixRepresentation import AdjacencyMatrix


def findComponents(graph,count,components,visited):
    for i  in range(n):
        if not visited[i]:
            count+=1
            dfs(i,count,visited,components)
    return count,components
def dfs(at,count,visited,components):
    visited[at]=True
    components[at] = count
    for i in g.get_adjacent_vertices(at):
        if not visited[i]:
            dfs(i,count,visited,components)



if __name__=='__main__':
    g = AdjacencyMatrix(7)
    #all the edges to be added
    # 1 - - 2    4 - - 5--0
    #  \   /      \   /
    #    3          6
    g.add_edge(1,2)
    g.add_edge(1,3)
    g.add_edge(2,3)
    g.add_edge(4,6)
    g.add_edge(4,5)
    g.add_edge(5,6)
    g.add_edge(5,0)
    n = g.numVertices
    count = 0
    components = [0 for i in range(n)]
    visited = [False for i in range(n)]
    counts,components = findComponents(g,count,components,visited)
    print(counts)
    for i,j in enumerate(components):
        print(i,'---->',j)
