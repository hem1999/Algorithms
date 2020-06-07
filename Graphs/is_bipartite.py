from AdjacencyMatrixRepresentation import AdjacencyMatrix

def is_bipartite(g):
    visited = [False for i in range(g.numVertices)]
    colors = ['black','white']
    colored = [None for i in range(g.numVertices)]
    colored[0]='black'
    dfs(0,visited,colored)


def dfs(at,visited,colored):
    visited[at]=True
    if colored[at]=='black':
        current_color ='White'
    else:
        current_color = 'black'
    for i in g.get_adjacent_vertices(at):
        if True:
            if colored[i]==colored[at]:
                print(f"Not a bipartite graph because of {i} and {at}")
                return False
            if not visited[i]:
                colored[i]=current_color
                dfs(i,visited,colored)

if __name__=='__main__':
    g = AdjacencyMatrix(6)
    #         2
    #      /    \
    #    /       \
    #  3 - - 0 - - 1
    #  |     |
    #  4 - - 5
    g.add_edge(0,1)
    g.add_edge(0,3)
    g.add_edge(0,5)
    g.add_edge(1,2)
    g.add_edge(2,3)
    g.add_edge(3,4)
    g.add_edge(4,5)
    colored = is_bipartite(g)
    print(colored)

    #Example of not a bipartite
    g = AdjacencyMatrix(6)
    #         2
    #      /    \
    #    /       \
    #  3 - - 0 - - 1
    #  |     |   /
    #  |     | /
    #  4 - - 5
    g.add_edge(0,1)
    g.add_edge(0,3)
    g.add_edge(0,5)
    g.add_edge(1,2)
    g.add_edge(2,3)
    g.add_edge(3,4)
    g.add_edge(4,5)
    g.add_edge(5,1)
    colored = is_bipartite(g)
    print(colored)
