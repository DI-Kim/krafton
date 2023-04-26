from sys import stdin as s

s = open('input.txt','rt')

N, M = map(int, s.readline().split())
tree = list(map(int, s.readline().split()))


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