import sys
input_list = list(map(int, sys.stdin.readline().split()))
N = input_list[0]
rec = input_list[1:]
print(N, rec)
area = 0
min_height = 1000000000
for i in rec:
    