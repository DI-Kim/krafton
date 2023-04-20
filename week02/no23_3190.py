import sys
from collections import deque

snake = deque()
N = int(sys.stdin.readline())
n = [[0] * N for _ in range(N)]
K = int(sys.stdin.readline())
for _ in range(K):
    i, j = map(int, sys.stdin.readline().split())
    n[i-1][j-1] = 1
    
L = int(sys.stdin.readline())
direction = deque()
for _ in range(L):
    a, b = sys.stdin.readline().split()
    a = int(a)
    direction.append([a, b])

my_direction = 3
count = 0
x = 0
y = 0
snake.append([x, y])
while True:
    count += 1
    # 방향 변하고 움직이는 거리
    if abs(my_direction % 12) == 3:
        y += 1
        if y > N-1: break
    elif abs(my_direction % 12) == 6:
        x += 1
        if x > N-1: break
    elif abs(my_direction % 12) == 9:
        y -= 1
        if y < 0: break
    elif abs(my_direction % 12) == 0:
        x -= 1
        if x < 0: break
    # 몸통 박치기 검사
    if len(snake) >= 4:
        if [x, y] in snake:
            break
    # 머리 디밀기
    snake.append([x, y])
    # 사과가 없으면 꼬리 자르기
    if n[x][y] != 1:
        snake.popleft()
    else:
        # 사과 먹으면 0으로
        n[x][y] = 0

    # 방향 전환
    if direction:
        if count == direction[0][0]:
            direct = direction.popleft()
            if direct[1] == 'L':
                # turn left
                my_direction -= 3
            else:
                # turn right
                my_direction += 3

print(count)