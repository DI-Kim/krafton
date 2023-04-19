import sys

N, B = map(int, sys.stdin.readline().split())
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))


def multiply(a, b):
    c = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                c[i][j] += (a[i][k] * b[k][j])
            c[i][j] %= 1000
    return c

def result(a, b):
    if b == 1:
        for i in range(len(a)):
            for j in range(len(a)):
                a[i][j] %= 1000
        return a
    
    half = b // 2
    temp = result(a, half)
    if b % 2 == 1:
        return multiply(multiply(temp, temp), A)
    else:
        return multiply(temp, temp)
    
answer = result(A, B)

for i in range(len(answer)):
    for j in range(len(answer)):
        print(answer[i][j], end=' ')
    print()