from sys import stdin as s
s = open('input.txt', 'r')
n = int(s.readline().strip())
a = list(map(int, s.readline().split()))
b = list(map(int, s.readline().split()))

a.sort()
b.sort(reverse=True)

sum = 0

for i in range(n):
    sum += a[i] * b[i]
print(sum)