from AdjacencyMatrixRepresentation import AdjacencyMatrix

def is_bipartite(g,colored,visited,pos):
    pass
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
