from sys import stdin as s
s = open('input.txt', 'r')

n, m = map(int, s.readline().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, s.readline().split())))

dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = graph[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]
        

for _ in range(m):
    x1, y1, x2, y2 = map(int, s.readline().split())
    result = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]

    print(result)
# for i in dp:
#     print(i)

    
