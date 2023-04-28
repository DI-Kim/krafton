from sys import stdin as s
s = open('input.txt', 'r')

n = int(s.readline().strip())
rest = 15746

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
    dp[i] %= rest
print(dp[n])