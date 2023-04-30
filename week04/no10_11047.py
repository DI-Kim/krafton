from sys import stdin as s
s = open('input.txt', 'r')
n, k = map(int, s.readline().split())
coins = []
for _ in range(n):
    coins.append(int(s.readline().strip()))
result = 0

coins.sort(reverse=True)
for i in coins:
    result += (k // i)
    k %= i
print(result)