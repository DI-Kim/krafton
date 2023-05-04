from sys import stdin as s
s = open('input.txt', 'r')

def search(x, visited):
    if visited == (1 << n) - 1:
        if graph[x][0]:
            return graph[x][0]
        else:
            return INF
        
    if dp[x][visited] != INF:
        return dp[x][visited]
    
    for i in range(1, n):
        if not graph[x][i]:
            continue
        if visited & (1 << i):
            continue

        dp[x][visited] = min(dp[x][visited], search(i, visited | (1 << i)) + graph[x][i])
    
    return dp[x][visited]

n = int(s.readline().strip())

INF = int(10 ** 9)
dp = [[INF] * (1 << n) for _ in range(n)]
graph = []

for _ in range(n):
    graph.append(list(map(int, s.readline().split())))

print(search(0, 1))