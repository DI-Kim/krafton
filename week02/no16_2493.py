import sys
from collections import deque

N = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
temp = deque()

# 뒤에서부터 진행, 시간 초과
# result = [0] * N

# for i in range(N-1, 0, -1):
#     temp.append([tower[i],i])
    
#     while temp:
#         value, location = temp.pop()

#         if  value <= tower[i - 1]:
#             result[location] = i
#         else:
#             temp.append([value, location])
#             break

# 앞부터 진행
result = []
for i in range(N):
    while temp:
        if temp[-1][0] >= tower[i]:
            result.append(temp[-1][1] + 1)
            break
        else:
            temp.pop()
    else:
        result.append(0)
    temp.append([tower[i],i])

    
for i in result:
    print(i, end=' ')
print()

