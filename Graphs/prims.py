import heapq
graph = [(0,1,4),
         (0,7,4),
         (1,7,11),
         (1,2,8),
         (2,3,7),
         (2,5,4),
         (2,8,2),
         (3,4,9),
         (3,5,14),
         (4,5,10),
         (5,6,2),
         (6,8,6),
         (6,7,1),
         (7,8,7)]#This is just for simplicity of typing
nodes = 9
def neighbours(i,matrix_rep):
    neighbour = []
    for j in range(len(matrix_rep[i])):
        if matrix_rep[i][j]!=0:
            neighbour.append(j)
    return neighbour
matrix_rep = [[0 for i in range(nodes)] for j in range(nodes)]
for i,j,w in graph:
    matrix_rep[i][j]=w
    matrix_rep[j][i]=w
vis_vertex = set()
vis_vertex.add(0)
mst = []
p_q = []
while(len(vis_vertex) != nodes):#
    for i in vis_vertex:
        for j in neighbours(i,matrix_rep):
            heapq.heappush(p_q,(i,j,matrix_rep[i][j]))
                # print("vis_vertex",vis_vertex)
    min_i,min_j,min_w = heapq.heappop(p_q)
    vis_vertex.add(min_j)
    mst.append((min_i,min_j,min_w))
    # print("mst",mst)
for item in mst:
    print(item)
