from sys import setrecursionlimit, stdin as s
from collections import deque

setrecursionlimit(100)
s = open('input.txt', 'r')

N, M = map(int, s.readline().split())
# goal = graph[N-1][M-1]
graph = []
queue = deque()

for _ in range(N):
    graph.append(list(map(int, s.readline().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

queue.append([0, 0])

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

for i in graph:
    print(i)
print(graph[N-1][M-1])