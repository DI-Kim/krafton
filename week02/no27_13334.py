import sys
import heapq

N = int(sys.stdin.readline())

hell = []
for _ in range(N):
    value = list(map(int, sys.stdin.readline().split()))
    value.sort()
    hell.append(value)
# 이중 반복문을 이용한 브루트포스 방식
# hell.sort()
# distance = int(sys.stdin.readline())

# 우선순위 큐 사용
distance = int(sys.stdin.readline())
roads = []
for i in hell:
    house, office = i
    if (office - house) <= distance:
        roads.append(i)
roads.sort(key = lambda x : x[1])
# print(roads)
max_hell = 0

# 이중 반복문을 이용한 브루트포스 방식
# for i in range(len(hell)):
#     temp = 0
#     for j in range(i, len(hell)):
#         if hell[i][0] + distance >= hell[j][1] and hell[j][0] >= hell[i][0]:
#             temp += 1
#         elif hell[j][0] > hell[i][0] + distance:
#             break
#     if temp > max_hell:
#         max_hell = temp

#우선순위 큐 사용
heap = []
for i in roads:
    if not heap:
        heapq.heappush(heap, i)
    else:
        while heap[0][0] < i[1] - distance:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, i)
    max_hell = max(max_hell, len(heap))
        

print(max_hell)