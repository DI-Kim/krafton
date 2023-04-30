from sys import stdin as s
s = open('input.txt', 'r')

n = int(s.readline().strip())
arr = list(map(int, s.readline().split()))
arr_num = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            if arr_num[j] + 1 > arr_num[i]:
                arr_num[i] = arr_num[j] + 1

print(max(arr_num))