import sys

n = int(sys.stdin.readline())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# print(paper)
count_list = []

def countPaper(n, x, y):
    count = paper[x][y]

    for i in range(x, x+ n):
        for j in range(y, y + n):
            if count != paper[i][j]:
                countPaper(n // 2, x, y)
                countPaper(n // 2, x + n // 2, y)
                countPaper(n // 2, x, y + n // 2)
                countPaper(n // 2, x + n // 2, y + n // 2)
                return
    
    if count == 1:
        count_list.append(1)
    else:
        count_list.append(0)

# print(len(paper))

countPaper(n, 0, 0)
one = 0
zero = 0
for i in count_list:
    if i == 1:
        one += 1
    else:
        zero += 1
print(zero, one)