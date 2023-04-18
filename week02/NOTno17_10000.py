# 바깥 영역 +1 하기
import sys
from collections import deque

N = int(sys.stdin.readline())
circles = []
stack = deque()
temp = []

count = 1 + N

for _ in range(N):
    circle = list(map(int, sys.stdin.readline().split()))
    circles.append([circle[0] - circle[1], circle[0] + circle[1]])

circles.sort(key=lambda x: (x[0], -x[1]))
print(circles)

# for i in circles:
#     while stack:
#         value = stack.pop()
#         temp.append(value)
#         if i == value:
#             count += 1
#             break

#         elif i[0] == value[0]:
#             stack.append([min(i[1], value[1]), max(i[1], value[1])])
#             break

#     stack.append(i)

value = circles[0]
for i in circles:
    
    while stack:
        value = stack.pop()
        
        for j in temp:
            if j[0] == value[0]:
                if j[0] == j[1]:
                    count += 1
                    temp.remove(j)
                j[0] = value[1]

        
        if i[0] == value[0]:
            # stack.append([min(i[1], value[1]), max(i[1], value[1])])
            temp.append([min(i[1], value[1]), max(i[1], value[1])])
            break

    stack.append(i)

for j in temp:
    if j == circles[-1]:
        j[0] = circles[-1][1]
for i in temp:
    if i[0] == i[1]:
        count+=1

print(count)
# 