from sys import stdin as s

# find 연산
def find_parent(x, parent):
    if x != parent[x]:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

#union 연산
def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a > b: parent[a] = b
    else: parent[b] = a


v, e = map(int, s.readline().split())
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

edges = []  # 간선 정보를 담을 리스트
total_cost = 0  # MST

for _ in range(e):
    a, b, cost = map(int, s.readline().split())
    edges.append([a, b, cost])
# 입력 받는 간선 정보를 비용을 오름차순 정렬
edges.sort(key = lambda x: x[2])

for i in range(e):
    a, b, cost = edges[i]
    if find_parent(a, parent) != find_parent(b, parent):
        union_parent(a, b, parent)
        total_cost += cost

print(total_cost)