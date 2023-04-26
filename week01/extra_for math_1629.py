import sys

def rest(a, b, c):
    mid = b // 2
    if b == 1:
        return a % c
    else:
        if b % 2 == 0:
            return (rest(a, mid, c) ** 2) % c
        else:
            return ((rest(a, mid, c) ** 2) * a) % c

a, b, c = map(int, sys.stdin.readline().split())
print(rest(a, b, c))