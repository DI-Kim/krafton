from sys import stdin as s
s = open('input.txt', 'r')

x = int(s.readline().strip())
y = int(s.readline().strip())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)