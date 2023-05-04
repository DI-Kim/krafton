from sys import stdin as s
from collections import deque
s = open('input.txt', 'r')

n = int(s.readline().strip())

maze = list(map(int, s.readline().split()))
dp = [0] * n
# print(maze)
count = 0
start = 0


queue = deque()
for i in range(n):
    queue.append(i)


        for j in range(i + 1, maze[i] + 1):
            if maze[j] >= n:
                print(maze)
                print(count)
                exit()
            if j < n:
                if maze[j] != 0 and visited[j] == 0:
                    maze[j] += maze[i]

                    queue.append(maze[j])
                    count += 1
            


