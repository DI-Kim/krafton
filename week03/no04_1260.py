from sys import stdin as s
from collections import deque

s = open('../input.txt', 'rt')

N, M, V = map(int, s.readline().split())

graph = [[0]*(N+1) for _ in range(N+1)] 

for _ in range(M):
    a, b = map(int, s.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs_visited = [0] * (N + 1)
bfs_visited = [0] * (N + 1)
stack = deque()


def dfs(v):
    dfs_visited[v] = 1
    print(v, end=' ')
    for i in range(1, N + 1):
        if dfs_visited[i] == 0 and graph[v][i] == 1:
            dfs(i)
    # dfs_visited[v] = 1
    # stack.append(v)
    # while stack:
    #     current = stack.pop()
    #     print(current, end=' ')
    #     for i in range(N, 0, -1):
    #         if not dfs_visited[i] and graph[current][i]:
    #             dfs_visited[i] = 1
    #             stack.append(i)

queue = deque()
def bfs(v):
    bfs_visited[v] = 1
    queue.append(v)
    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for i in range(1, N + 1):
            if not bfs_visited[i] and graph[current][i]:
                bfs_visited[i] = 1
                queue.append(i)

                
dfs(V)
print()
bfs(V)
print()
# print(result)
# print(dfs_visited)
