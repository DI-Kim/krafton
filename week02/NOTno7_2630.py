import sys

n = int(sys.stdin.readline())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# print(paper)
count = 0

def countPaper(n, x, y):
    if n == 1:
        count += 1
        return
    for i in range(len(paper)):
        for j in range(len(paper[i])):
            print(i, j)
    
# print(len(paper))

countPaper(0, 0, 0)