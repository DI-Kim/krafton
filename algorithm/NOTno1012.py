from sys import stdin as s
from collections import deque
s= open('input.txt', 'r')

test_num = int(s.readline().strip())
m, n, k = map(int, s.readline().split())

graph = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
for _ in range(k):
    i, j = map(int, s.readline().split())
    graph[j][i] = 1



def bfs():
    test_queue = deque()
    queue = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue.append([0, 0])
    visited[0][0] = 1
    if graph[0][0] == 1:
        count = 1
    else:
        count = 0
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                    if graph[nx][ny] == 1:
                        test_queue.append([nx, ny])
                        count += 1
                        while test_queue:
                            i, j = test_queue.popleft()
                            for i in range(4):
                                ni = i + dx[i]
                                nj = j + dy[i]
                                if 0 <= ni < n and 0 <= nj < m:
                                    if visited[nx][ny] == 0:
                                        if graph[ni][nj] == 0:
                                            continue
                                        else:
                                            visited[ni][nj] = 1
                                            test_queue.append([ni, nj])

    print(count)
bfs()

for i in graph:
    print(i)
for i in visited:
    print(i)
