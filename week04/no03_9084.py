from sys import stdin as s
s = open('input.txt', 'r')
test_num = int(s.readline().strip())

for _ in range(test_num):
    n = int(s.readline().strip())
    coins = list(map(int, s.readline().split()))
    m = int(s.readline().strip())
    dp = [0] * (m + 1)
    dp[0] = 1

    for i in coins:
        for j in range(m + 1):
            if j - i >= 0:
                dp[j] += dp[j - i]
    print(dp[m])
        