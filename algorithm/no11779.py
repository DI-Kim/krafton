from sys import stdin as s
import heapq
s = open('input.txt', 'r')

INF = int(10 ** 8)
city_num = int(s.readline().strip())
bus_num = int(s.readline().strip())
distances = [INF] * (city_num + 1)
graph = [[] for _ in range(city_num + 1)]
for _ in range(bus_num):
    start, end, cost = map(int, s.readline().split())
    graph[start].append((end, cost))

start_city, destination = map(int, s.readline().split())
predeccessor = [start_city] * (city_num + 1)

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (start, 0))
    distances[start] = 0

    while heap:
        current, distance = heapq.heappop(heap)

        if distances[current] < distance:
            continue

        for i in graph[current]:
            cost = distance + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                predeccessor[i[0]] = current 
                heapq.heappush(heap, (i[0], cost))

dijkstra(start_city)

print_destination = []
temp = destination
while temp != start_city:
    print_destination.append(temp)
    temp = predeccessor[temp]

print_destination.append(start_city)

print(distances[destination])
print(len(print_destination))
for i in range(len(print_destination) - 1, -1, -1):
    print(print_destination[i], end=' ')
print()