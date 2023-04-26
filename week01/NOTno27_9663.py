import sys

def isPossible(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True


def NQueen(i):
    global result
    if i == N:
        result += 1
        return
    
    else:
        for j in range(N):
            if visited[i]:
                continue
            row[i] = j
            if isPossible(i):
                visited[i] = True
                NQueen(i + 1)
                visited[i] = False


N = int(sys.stdin.readline())
# N = 4
row = [0] * N
visited = [False] * N
result = 0
NQueen(0)
print(result)