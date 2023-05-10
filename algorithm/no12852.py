from sys import stdin as s
s = open('input.txt', 'r')

n = int(s.readline().strip())

graph = [1] * (n+1)
graph[0] = 0
graph[1] = 0
predeccessor = [0] * (n+1)

for i in range(2, n+1):
    result = 10 ** 6
    # predeccessor = 3
    if i % 3 == 0:
        if graph[i//3] + 1 < result:
            result = graph[i//3] + 1
            predeccessor[i] = 3
    # preccessor = 2
    if i % 2 == 0:
        if graph[i//2] + 1 < result:
            result = graph[i//2] + 1
            predeccessor[i] = 2
    # predeccessor = 0
    if graph[i-1] + 1 < result:
        result = graph[i-1] + 1
        predeccessor[i] = 0
    graph[i] = result

print(graph[n])
print(n, end=' ')
while n > 1:
    if predeccessor[n] == 0:
        n -= 1
    elif predeccessor[n] == 2:
        n //= 2
    else:
        n //= 3
    print(n, end=' ')
print()