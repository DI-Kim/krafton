from sys import stdin as s

s = open('input.txt', 'r')
n = int(s.readline().strip())
graph = [0] + list(map(int, s.readline().split()))
# print(graph)
dp = [[1, i] for i in range(n + 1)]
dp[0][0] = 0
dp_info = []

result = 1
for i in range(1, n + 1):
    for j in range(1, i):
        if graph[j] < graph[i]:
            if dp[j][0] + 1 > dp[i][0]:
                dp[i][0] = dp[j][0] + 1
                dp[i][1] = j
                
            if dp[i][0] > dp[result][0]:
                result = i

# print(result)
# print(dp)
print(dp[result][0])

while True:
    dp_info.append(graph[result])
    if result != dp[result][1]:
        result = dp[result][1]
    else: break


for i in range(len(dp_info)-1, -1, -1):
    print(dp_info[i], end=' ')
print()