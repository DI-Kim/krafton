from sys import stdin as s
import sys
sys.setrecursionlimit(10**6)
s = open('../input.txt', 'r')

v = int(s.readline().strip())
visited = [0] * (v+1)
graph = [[] for _ in range(v+1)]
for _ in range(v-1):
    i, j = map(int, s.readline().split())
    graph[i].append(j)
    graph[j].append(i)

result = []
def dfs(node, predecessor = None):
    visited[node] = 1
    result.append([node, predecessor])
    for i in graph[node]:
        if visited[i] == 0:
            dfs(i, node)

dfs(1)

result = result[1:]
result.sort()
for i, j in result:
    print(j)