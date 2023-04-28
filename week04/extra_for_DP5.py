n, m = 3, 42
coins = [3, 5, 7]
dp = [0] * (m + 1)
for i in coins:
    if len(dp) -1 >= i:
        dp[i] = 1

for i in range(1, m + 1):
    for j in coins:
        if i - j > 0 and dp[i-j] != 0:
            if dp[i] == 0:
                dp[i] = dp[i - j] + 1
            if dp[i] > dp[i - j] + 1:
                dp[i] = dp[i - j] + 1
    
if dp[m] == 0:
    print( -1)
else:
    print(dp[m])