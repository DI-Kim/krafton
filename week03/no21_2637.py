from collections import deque
from sys import stdin as s
s = open('input.txt', 'r')

n = int(s.readline().strip())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
part = [[0] * (n + 1) for _ in range(n + 1)]
m = int(s.readline().strip())
for _ in range(m):
    x, y, k = map(int, s.readline().split())
    graph[y].append([x, k])
    indegree[x] += 1

# print(graph)

def topological_sort():
    queue = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        current = queue.popleft()

        for part_num, part_quantity in graph[current]:
            if part[current].count(0) == n + 1:
                part[part_num][current] += part_quantity
            else:
                for i in range(1, n + 1):
                    part[part_num][i] += part[current][i] * part_quantity


            indegree[part_num] -= 1
            if indegree[part_num] == 0:
                queue.append(part_num)

topological_sort()

for i in enumerate(part[n]):
    if i[1] > 0:
        print(i[0], i[1])


