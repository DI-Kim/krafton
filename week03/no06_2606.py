from sys import stdin as s
s = open('../input.txt', 'rt')

v = int(s.readline().strip())
e = int(s.readline().strip())
edges = []
parent = [0] * (v + 1)
for i in range(1, v+1):
    parent[i] = i

def find(start):
    if start != parent[start]:
        parent[start] = find(parent[start])
    return parent[start]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b: parent[a] = b
    else: parent[b] = a

for _ in range(e):
    edge = list(map(int, s.readline().split()))
    edges.append(edge)
edges.sort()

for _ in range(2):  # 두번 반복 말고 해결 방법 찾아보기
    for i in range(e):
        a, b = edges[i]
        if find(a) != find(b):
            union(a, b)

result = -1
for i in parent:
    if i == 1:
        result += 1

print(result)