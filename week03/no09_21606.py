# 다시 한번 풀어보기
# 푸는 방법에 대해 고민해보기
from sys import setrecursionlimit, stdin as s
setrecursionlimit(10**9)
s = open('input.txt', 'r')

N = int(s.readline().strip())

status = [0] + list(map(int, s.readline().strip()))
result = 0
visited = [0] * (N+1)
graph = [[]for _ in range(N + 1)]
for _ in range(N-1):
    i, j = map(int, s.readline().split())
    graph[i].append(j)
    graph[j].append(i)
    if status[i] == 1 and status[j] == 1:
        result += 2

def dfs(node, result):
    visited[node] = 1
    for i in graph[node]:
        if visited[i] == 0 and status[i] == 0:
            result = dfs(i, result)
        elif status[i] == 1:
            result += 1
    return result

for i in range(1, N+1):
    if status[i] == 0 and visited[i] == 0:
        count = dfs(i, 0)
        result += count * (count - 1)
print(result)
    

