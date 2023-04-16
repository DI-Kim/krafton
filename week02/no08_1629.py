import sys
a, b, c = map(int, sys.stdin.readline().split())

def multiply(x, y, z):
    half = y // 2
    if y == 1:
        return x % z
    
    if y % 2 == 0:
        return (multiply(x, half, z) ** 2) % z
    else:
        return (multiply(x, half, z) ** 2) * x % z

print(multiply(a, b, c))