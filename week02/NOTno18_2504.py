import sys
from collections import deque

string = sys.stdin.readline()
stack = deque()
for i in string:
    stack.append(i)
result = 0

def small():
    global result
    if not stack:
        result = 0
        return 0
    value = stack.pop()
    if value == '(':
        return 2
    elif value == '[':
        result = 0
        stack.clear()
        return 0
    elif value == ']':
        a = middle()
        if not stack:
            return 0
        temp = stack.pop()
        if temp == '(':
            return (2 * a)
        elif temp == ')':
            return (2 * (a + small()))
        elif temp == ']':
            return (2 * (a + middle()))
    elif value == ')':
        a = small()
        if not stack:
            return 0
        temp = stack.pop()
        if temp == '(':
            return (2 * a)
        elif temp == ')':
            return (2 * (a + small()))
        elif temp == ']':
            return (2 * (a + middle()))
    
def middle():
    global result
    if not stack:
        result = 0
        return 0
    value = stack.pop()
    if value == '(':
        result = 0
        stack.clear()
        return 0
    elif value == '[':
        return 3
    elif value == ']':
        a = middle()
        if not stack:
            return 0
        temp = stack.pop()
        if temp == '[':
            return (3 * a)
        elif temp == ')':
            return (3 * (a + small()))
        elif temp == ']':
            return (3 * (a + middle()))
    elif value == ')':
        a = small()
        if not stack:
            return 0
        temp = stack.pop()
        if temp == '[':
            return (3 * a)
        elif temp == ')':
            return (3 * (a + small()))
        elif temp == ']':
            return (3 * (a + middle()))

while stack:
    if len(stack) % 2 == 0:
        value = stack.pop()
        if value == ']':
            result += middle()
        elif value == ')':
            result += small()
    else:
        break

print(result)