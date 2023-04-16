import sys
from collections import deque

stack = deque()

K = int(sys.stdin.readline())

for _ in range(K):
    value = int(sys.stdin.readline())
    if value != 0:
        stack.append(value)
    else:
        stack.pop()
print(sum(stack))