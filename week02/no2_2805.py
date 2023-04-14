import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))


start = 0
end = max(tree)

while start <= end:
    count = 0
    mid = (start + end) // 2

    for i in tree:
        if i > mid:
            count += (i - mid)
    if count >= M:
        start = mid + 1
    else:
        end = mid - 1
    
print(end)