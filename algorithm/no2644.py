from collections import deque
from sys import stdin as s
s = open('input.txt', 'r')

n = int(s.readline().strip())
person1, person2 = map(int, s.readline().split())
m = int(s.readline().strip())

visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j = map(int, s.readline().split())
    graph[i].append(j)
    graph[j].append(i)

# dfs
connect = False
count = 0
stack = deque()
stack.append(person1)
visited[person1] = 1
def dfs():
    global count, connect
    current = stack.pop()
    if current == person2:
        connect = True
        print(count)
        return
    
    for i in graph[current]:
        if visited[i] == 0:
            visited[i] = 1
            stack.append(i)
            count += 1
            dfs()
            count -= 1
dfs()
if not connect:
    print(-1)
