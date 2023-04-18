import sys
from collections import deque

string = sys.stdin.readline()
stack = deque()
temp = 1
result = 0

for i in range(len(string)):
    value = string[i]
    if value == '(':
        temp *= 2
        stack.append(value)

    elif value == '[':
        temp *= 3
        stack.append(value)

    elif value == ')':
        # string[i - 1] 했을 때 반례 ([())]
        # if not stack or string[i - 1] == '[':
        if not stack or stack[-1] == '[':
            result = 0
            break
        if string[i - 1] == '(':
            result += temp
        # temp를 들어올때마다 나눠줘야 괄호가 끝나고 temp = 1로 유지가 됨
        # 이미 더할 때 괄호의 곱이 유지가 되서 마지막 닫을 때는 temp를 1로 만듦
        temp = temp // 2
        stack.pop()

    elif value == ']':
        # if not stack or string[i - 1] == '(':
        if not stack or stack[-1] == '(':
            result = 0
            break
        if string[i - 1] == '[':
            result += temp
        temp = temp // 3
        stack.pop()

if stack:
    result = 0
print(result)