from sys import stdin as s
s = open('input.txt', 'r')

n = s.readline().strip()
m = s.readline().strip()
lenn = len(n)
lenm = len(m)

arr = [[0] * (lenm + 1) for _ in range(lenn + 1)]

for i in range(1, lenn + 1):
    for j in range(1, lenm + 1):
        if n[i - 1] == m[j - 1]:
            arr[i][j] = arr[i - 1][j - 1] + 1
        else:
            arr[i][j] = max(arr[i][j - 1], arr[i - 1][j])
print(arr[-1][-1])