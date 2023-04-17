import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
input_value = list(sys.stdin.readline().strip())
stack = deque()
k = K

for i in range(N):

    while stack and k > 0:
        if input_value[i] > stack[-1]:
            stack.pop()
            k -= 1
        else:
            break
    stack.append(input_value[i])
    
while N-K != len(stack):
    stack.pop()

for i in stack:
    print(i, end='')
print()
