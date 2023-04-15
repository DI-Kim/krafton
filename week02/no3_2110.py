# 최소거리와 최대거리를 구한 후, 이분탐색을 이용하여 적정거리를 구한다.
import sys

n, c = map(int, sys.stdin.readline().split())
houses = []
for i in range(n):
    houses.append(int(sys.stdin.readline().strip()))
houses.sort()

# 최소 거리
start = 1
# 최대 거리
end = houses[-1] - houses[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    current = houses[0]
    count = 1

    for i in range(1, len(houses)):
        if houses[i] >= current + mid:
            count += 1
            current = houses[i]
    
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1


print(result)