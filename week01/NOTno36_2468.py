import sys
from collections import deque
sys.setrecursionlimit(10**6)
"""
이차원 배열을 입력 받는다.
2 ~100 까지의 for 문을 돌면서 i보다 작은 수를 0으로 만드는 배열을 새로 생성한다.
for 문을 돌면서 0(False)이 아닌 인덱스를 찾으면,
    그 인덱스에서 인접한 0이 아닌 인덱스를 찾고 값을 0으로 바꾼다.
인접한 인덱스를 찾을 때 배열 자체를 벗어나지 않도록 주의한다. 0 <= i <= N, 0 <= j <= N
인접한 0이 아닌 모든 인덱스를 찾았으면 안전구역(count) +1 을 한다.
안전구역 count를 출력한다.
"""
def makeTrue(i, j):
    safety_area[i][j] = True
    
def findPath(x, y):
    for k in range(4):
        new_x = x + dx[k]
        new_y = y + dy[k]
        
        if 0 > new_x or new_x >= N or 0 > new_y or new_y >= N:
            continue
        elif safety_area[new_x][new_y]:
            continue
        else:
            makeTrue(new_x, new_y)
            findPath(new_x, new_y)

result = 1

N = int(sys.stdin.readline())
input_list = []
for _ in range(N):
    input_list.append(list(map(int, sys.stdin.readline().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]



for i in range(1, 101):
    count = 0
    safety_area = [[False] * N for _ in range(N)]

    for x in range(N):
        for y in range(N):
            if input_list[x][y] - i <= 0:
                makeTrue(x, y)
    
    for x in range(N):
        for y in range(N):
            if not safety_area[x][y]:

                makeTrue(x, y)
                findPath(x, y)
                count += 1
    
    result = max(result, count)

print(result)