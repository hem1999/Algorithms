import itertools
N = int(input())
graph = {}
for i in range(N):
    graph[i] = list(map(int,input().split()))
router_m,router_n = tuple(map(int,input().split()))

def find_all_paths(graph, start, end, path=[]):

    path = path + [start]
    if start == end:
        return [path]
    if not start in graph.keys():
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
print(find_all_paths(graph,router_m,router_n,)
