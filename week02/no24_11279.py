import heapq
import sys

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    input_num = int(sys.stdin.readline())
    if input_num == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -input_num)