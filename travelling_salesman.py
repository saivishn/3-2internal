from sys import maxsize
from itertools import permutations
V=4
def solution(graph,s):
    vertex=[]
    for i in range(V):
        if(i!=s):
            vertex.append(i)
    min_path=maxsize
    n=permutations(vertex)
    for i in n:
        current_path=0
        k=s
        for j in i:
            current_path+=graph[k][j]
            k=j
        current_path+=graph[k][s]
        min_path=min(min_path,current_path)
    return min_path
graph = [[0, 10, 15, 20], [5,0,9,10],[6,13,0,12], [8,8,9,0]]
s = 0
print(solution(graph, s))