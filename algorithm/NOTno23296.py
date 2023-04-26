# 사이클이 두개면 틀릴 가능성이 매우 높음
# DAG 이용해서 풀어보기!
from collections import deque
from sys import stdin as s
s = open('input.txt', 'r')

N = int(s.readline().strip())
A = [0] + list(map(int, s.readline().split()))
visited = [0] * (N+1)
count = 0
result = []
visited[1] = 1
def dfs(node):
    global count
    current = node
    visited[node] = 1
    count += 1
    result.append(A[node])
    if visited[A[node]] == 0:
        dfs(A[node])

dfs(1)
for i in range(1, len(visited)):
    if visited[i] == 0 and visited[A[i]] == 1:
        visited[i] = 1
        result.append(i)
        result.append(A[i])
        count += 2
    elif visited[i] == 0 and visited[A[i]] == 0:
        visited[i] = 1
        result.append(i)
        count += 1


print(count)
for i in result:
    print(i, end = ' ')
print()