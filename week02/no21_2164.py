import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
queue.extend(i for i in range(1, N + 1))

for _ in range(N-2):
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())
