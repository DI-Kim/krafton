import sys
N = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().split()))

result = [1] * N

for i in range(len(input_list)):
    for j in range(i):
        if input_list[i] > input_list[j]:
            result[i] = max(result[j] + 1, result[i])
print(max(result))