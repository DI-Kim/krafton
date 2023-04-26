# 행렬의 시작은 0부터... 1부터 아님!
N, r, c = map(int, input().split())
# N: 2^N의 배열, r: 행 (세로), c: 열 (가로)
result = 0
while N > 1:
    size = 2 ** (N - 1)

    if c // size == 1 and r // size == 0:
        result += size ** 2 * 1
        c %= size

    elif r // size == 1 and c // size == 0:
        result += size ** 2 * 2
        r %= size
    elif r // size == 1 and c // size == 1:
        result += size ** 2 * 3
        c %= size
        r %= size
    else:
        pass
    N -= 1

if r == 0 and c == 0:
    pass
elif r == 0 and c == 1:
    result += 1
elif r == 1 and c == 0:
    result += 2
elif r == 1 and c == 1:
    result += 3
    
print(result)