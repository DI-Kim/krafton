import sys

n, m = map(int, sys.stdin.readline().split())
input_list = []
visited = [False] * n

def find(start):
    if len(input_list) == m:
        for i in input_list:
            print(i, end=' ')
        print()
    
    else:
        for i in range(start, n + 1):
            if not visited[i-1]:
                input_list.append(i)
                visited[i-1] = True
                find(start+1)
                input_list.pop()
                visited[i-1] = False

find(1)