from sys import stdin as s
from collections import deque

s = open('input.txt', 'r')
r, c = map(int, s.readline().split())
graph = []
distance = [[0] * c for _ in range(r)]
for _ in range(r):
    line = list(s.readline().strip())
    graph.append(line)

queue = deque()
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            queue.append([i, j])
        elif graph[i][j] == 'D':
            a, b = i, j
        

for i in range(r):
    for j in range(c):
        if graph[i][j] == '*':
            queue.append([i, j])


result = 'KAKTUS'
def bfs():
    global result
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()

        if graph[a][b] == 'S':
            result = distance[a][b]
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if graph[x][y] == 'S':
                    if graph[nx][ny] == '.' or graph[nx][ny] == 'D':
                        distance[nx][ny] = distance[x][y] + 1
                        graph[nx][ny] = 'S'
                        queue.append([nx, ny])

                
                elif graph[x][y] == '*':
                    if graph[nx][ny] == '.'or graph[nx][ny] == 'S':
                        graph[nx][ny] = '*'
                        queue.append([nx, ny])
bfs()

print(result)