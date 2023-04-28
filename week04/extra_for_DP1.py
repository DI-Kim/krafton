n = int(input())
fib = [0] * (n + 1)
# top-down
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if fib[x] != 0:
        return fib[x]
    fib[x] = fibo(x - 1) + fibo(x - 2)
    return fib[x]

print(fibo(n))

# bottom-up
dp = [0] * (n + 1)
dp[1] = 1
dp[2] = 1

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])