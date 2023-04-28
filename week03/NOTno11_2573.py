from collections import deque
from sys import stdin as s
s = open('input.txt', 'r')
n, m = map(int, s.readline().split())
visited = [[0]* m for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(map(int, s.readline().split())))

# for i in graph:
#     print(i)

def bfs():
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    if graph[nx][ny] == 0:
                        queue.append([nx, ny])
                    if graph[nx][ny] > 0:
                        queue.appendleft([nx, ny])
                        for i in range(4):
                            ax = nx + dx[i]
                            ay = ny + dy[i]
                            if graph[ax][ay] == 0 and graph[nx][ny] > 0:
                                graph[nx][ny] -= 1
bfs()
for i in graph:
    print(i)
for i in visited:
    print(i)