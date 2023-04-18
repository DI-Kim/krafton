import sys
import heapq

N = int(sys.stdin.readline())

small = []
big = []

for _ in range(N):
    number = int(sys.stdin.readline())
    if len(big) == len(small):
        heapq.heappush(small, -number)
    else:
        heapq.heappush(big, number)
    
    # 짝수 개를 불렀을 때 작은 값 말하기
    # if (len(small) + len(big)) % 2 == 0:
    if big:
        small_value = -small[0]
        big_value = big[0]
    
        if small_value > big_value:
            heapq.heappush(big, -heapq.heappop(small))
            heapq.heappush(small, -heapq.heappop(big))
          
    print(-small[0])
