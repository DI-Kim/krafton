n = 4
storage = [1, 3, 1, 5]

dp = [0] * n
dp[0] = storage[0]
dp[1] = storage[1]
if dp[0] > dp[1]:
    dp[1] = dp[0]

for i in range(2, n):
    dp[i] = dp[i - 1]

    if dp[i - 2] + storage[i] > dp[i]:
        dp[i] = dp[i - 2] + storage[i]
print(dp[-1])
print(dp)