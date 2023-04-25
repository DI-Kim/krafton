from collections import deque
from sys import stdin as s
s = open('input.txt', 'r')

N, M = map(int, s.readline().split())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, s.readline().split())
    indegree[j] += 1
    graph[i].append(j)

def topological_sort():
    queue = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        current = queue.popleft()
        print(current, end = ' ')

        for i in graph[current]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

topological_sort()
print()