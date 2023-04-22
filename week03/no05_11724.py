from sys import stdin as s
s = open('../input.txt', 'r')

v, e = map(int, s.readline().split())
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i
edges = []

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b: parent[a] = b
    else: parent[b] = a
    

for _ in range(e):
    a, b = map(int, s.readline().rstrip().split())
    edges.append([a, b])
edges.sort()

for _ in range(2):  # 다른 솔루션 생각해보기
    for i in range(e):
        a, b = edges[i]
        if find(a) != find(b):
            union(a, b)

print(len(set(parent[1:])))