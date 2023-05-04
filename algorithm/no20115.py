from sys import stdin as s
s = open('input.txt', 'r')

n = int(s.readline().strip())

drink = list(map(int, s.readline().split()))
drink.sort()

final = drink[-1]
for i in drink[:n-1]:
    final += (i / 2)

print(final)