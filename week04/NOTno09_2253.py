from sys import stdin as s
s = open('input.txt', 'r')

n, m = map(int, s.readline().split())
stone = [0] * (n + 1)
jump = 1
count = 0
for _ in range(m):
    stone[int(s.readline().strip())] = -1

print(stone)
for i in range(2, n + 1):
    pass
