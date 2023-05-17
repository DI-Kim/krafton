from sys import stdin as s
s = open('input.txt', 'r')

def dfs(count, result, visited, x, y):
    global answer
    if count == 3:
        answer = max(result, answer)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            # ㅗ 모양 찾기
            visited[nx][ny] = 1
            if count == 1:
                # visited[nx][ny] = 1
                dfs(count + 1, result + graph[nx][ny], visited, x, y) 
                visited[nx][ny] = 0
            dfs(count + 1, result + graph[nx][ny], visited, nx, ny)
            visited[nx][ny] = 0

n, m = map(int, s.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, s.readline().split())))
visited = [[0] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(0, graph[i][j], visited, i, j)
        visited[i][j] = 0
print(answer)