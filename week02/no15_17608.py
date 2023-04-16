import sys
from collections import deque

stack = deque()
N = int(sys.stdin.readline())
count = 0

for _ in range(N):
    stack.append(int(sys.stdin.readline()))

highest_building = stack.pop()
count += 1

for _ in range(len(stack)):
    building = stack.pop()
    if building > highest_building:
        count += 1
        highest_building = building
print(count)