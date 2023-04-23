from sys import stdin as s
import sys
sys.setrecursionlimit(10**9)
s = open('../input.txt', 'r')

# visited num을 1과 2로 구분하여 붙어 있으면 이분그래프가 아님
def dfs(node, num):
    global bipartite
    if bipartite == True:
        return
    color = 3 - num
    visited[node] = color

    for i in graph[node]:
        if color == visited[i]:
            bipartite = True
            return
        if not visited[i]:
            dfs(i, color)
    

test_num = int(s.readline())

for _ in range(test_num):
    v, e = map(int, s.readline().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    bipartite = False
    for _ in range(e):
        a, b = list(map(int, s.readline().split()))
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, v+1):
        if bipartite == True:
            break
        if not visited[i]:
            dfs(i, 1)
    if bipartite:
        print('NO')
    else:
        print('YES')