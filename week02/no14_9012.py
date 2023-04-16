import sys
from collections import deque


test_num = int(sys.stdin.readline())

for _ in range(test_num):
    stack = deque()
    input_case = sys.stdin.readline()
    for i in input_case:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                stack.append(1)
                break
            stack.pop()
    if not stack:
        print('YES')
    else:
        print("NO")