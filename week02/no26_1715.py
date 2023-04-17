import sys
import heapq

N = int(sys.stdin.readline())

heap = []

for _ in range(N):
    heapq.heappush(heap, int(sys.stdin.readline()))

# result = heapq.heappop(heap) * (len(heap))
# for i in range(len(heap), 0, -1):
#     result += (heapq.heappop(heap) * i)
# print(result)

result = 0
if len(heap) == 1:
    print(0)
else:
    while len(heap) > 1:
        sum_value = heapq.heappop(heap) + heapq.heappop(heap)
        result += sum_value
        heapq.heappush(heap, sum_value)
    print(result)