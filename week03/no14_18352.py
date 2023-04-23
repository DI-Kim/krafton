from sys import stdin as s
from collections import deque
s = open('../input.txt', 'r')
# City: 도시 개수, Road: 도로 개수, Distance: 거리, Start: 출발 도시
City, Road, Distance, Start = map(int, s.readline().split())

graph = [[]for _ in range(City + 1)]
for _ in range(Road):
    a, b = map(int, s.readline().split())
    graph[a].append(b)

distance = [0] * (City + 1)
visited = [False] * (City + 1)
queue = deque()
answer = []

visited[Start] = True
distance[Start] = 0
queue.append(Start)

while queue:
    current = queue.popleft()

    for i in graph[current]:
        if not visited[i]:
            visited[i] = True
            queue.append(i)
            distance[i] = distance[current] + 1
            if distance[i] == Distance:
                answer.append(i)

answer.sort()
if answer:
    for i in answer:
        print(i)
else:
    print(-1)