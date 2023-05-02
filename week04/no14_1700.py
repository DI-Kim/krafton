from sys import stdin as s
s = open('input.txt', 'r')

n, k = map(int, s.readline().split())
input_list = list(map(int, s.readline().split()))

graph = [0] * n
count = 0

for i in range(k):
    if input_list[i] in graph:
        continue
    else:
        if 0 in graph:
            for j in range(n):
                if graph[j] == 0:
                    graph[j] = input_list[i]
                    break
        else:
            temp = 0
            far = 0
            for j in range(n):
                if graph[j] not in input_list[i:]:
                    temp = j
                    break
                a = input_list[i:].index(graph[j])
                if a > far:
                    far = a
                    temp = j
                    
            graph[temp] = input_list[i]
            count += 1
                    
print(count)
