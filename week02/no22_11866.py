import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
queue = deque(i for i in range(1, N + 1))
result = []

for _ in range(N):
    for _ in range(K - 1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

res_str = '<'

for i in result:
    res_str += (str(i) + ', ')
res_str = res_str[:-2] 
res_str += '>'
print(res_str)