from collections import deque
from sys import stdin as s
s= open('../input.txt', 'r')
# N: 도시 개수, M: 버스 개수
N = int(s.readline().strip())
M = int(s.readline().strip())
bus = [[] for _ in range(N + 1)]

for _ in range(M):
    b = list(map(int, s.readline().split()))
    #b[0]: 출발 도시, b[1]: 도착 도시, b[2]: 비용
    bus[b[0]].append([b[1], b[2]])

departure, arrive = map(int, s.readline().split())

distances = [10**9] * (N + 1)
queue = deque()
queue.append([departure, 0])
distances[departure] = 0

while queue:
    cur_destination, cur_distance = queue.popleft()

    if distances[cur_destination] < cur_distance:
        continue
    for new_destination, new_distance in bus[cur_destination]:
        distance = cur_distance + new_distance
        if distance < distances[new_destination]:
            distances[new_destination] = distance
            queue.append([new_destination, distance])

    
print(distances[arrive])