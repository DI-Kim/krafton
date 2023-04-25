from collections import deque
from sys import stdin as s
s = open('input.txt', 'r')

# N: 정점, M: 간선, V: start
N, M, V = map(int, s.readline().split())
graph = [[]for _ in range(N + 1)]
for _ in range(M):
    i, j = map(int, s.readline().split())
    graph[i].append(j)
    graph[j].append(i)
for i in graph:
    i.sort()


# dfs
dfs_visited = [0] * (N + 1)
stack = deque()
stack.append(V)
dfs_visited[V] = 1
def dfs():
    current = stack.pop()
    print(current, end=' ')
    for i in graph[current]:
        if dfs_visited[i] == 0:
            dfs_visited[i] = 1
            stack.append(i)
            dfs(i)
dfs()
print()

# bfs
def bfs():
    queue = deque()
    bfs_visited = [0] * (N + 1)
    queue.append(V)
    bfs_visited[V] = 1
    
    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for i in graph[current]:
            if bfs_visited[i] == 0:
                bfs_visited[i] = 1
                queue.append(i)
bfs()
print()