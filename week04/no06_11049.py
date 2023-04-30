from sys import stdin as s
s = open('input.txt', 'r')
n = int(s.readline().strip())
matrix = []
dp = [[0] * n for _ in range(n)]
for _ in range(n):
    matrix.append(list(map(int, s.readline().split())))

for l in range(1, n):
    for i in range(n - l):
        j = i + l
        dp[i][j] = (2 ** 31)

        for k in range(i, j):
            q = dp[i][k] + dp[k+1][j] + (matrix[i][0] * matrix[k+1][0] * matrix[j][1])
            if q < dp[i][j]:
                dp[i][j] = q
        

print(dp[0][n-1])