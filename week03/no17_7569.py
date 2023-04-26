# bfs 먼저 구현
# 입력 받는 함수 자체를 방문 배열로 생각해보자
# x, y, z 방향으로 다 갈 수 있게 구현 3차원으로!
# 날짜 그래프 하나 더 만들기
from sys import stdin as s
from collections import deque
s = open('input.txt', 'r')
m, n, h = map(int, s.readline().split())
graph = []

for _ in range(h):
    line_stack = []
    for _ in range(n):
        line = list(map(int, s.readline().split()))
        line_stack.append(line)
    graph.append(line_stack)

day_graph = [[[0] * m for _ in range(n)]for _ in range(h)]

def bfs():
    
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    queue = deque()
    # z, x, y
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    queue.append([i, j, k])

    while queue:
        z, x, y= queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = 1
                    day_graph[nz][nx][ny] = day_graph[z][x][y] + 1
                    queue.append([nz, nx, ny])
                else:
                    continue

    result = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    print(-1)
                    exit()
                if day_graph[i][j][k] > result:
                    result = day_graph[i][j][k]
    print(result)
bfs()