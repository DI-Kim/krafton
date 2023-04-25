# 1을 먼저 탐색하기 위해 appendleft!
from collections import deque
from sys import stdin as s
s = open('input.txt', 'r')

n = int(s.readline().strip())
graph = []
# visited 가 10억이면 아직 방문 아님
visited = [[-1] * (n) for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, s.readline().strip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
queue.append((0,0))
visited[0][0] = 0

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == -1:
                if graph[nx][ny] != 0:
                    queue.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

print(visited[n-1][n-1])