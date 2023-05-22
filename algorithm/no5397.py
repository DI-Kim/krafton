from collections import deque
from sys import stdin as s
s = open('input.txt', 'r')

test_num = int(s.readline().strip())

for _ in range(test_num):
    pw_input = s.readline().strip()
    stack = deque()
    temp = deque()

    for i in pw_input:
        if i == '<':
            if stack:
                temp.append(stack.pop())
        elif i == '>':
            if temp:
                stack.append(temp.pop())
        elif i == '-':
            if stack:
                stack.pop()
        else:
            stack.append(i)

    stack.extend(reversed(temp))

    print(''.join(stack))
