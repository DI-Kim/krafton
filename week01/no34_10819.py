import sys

test_num = int(sys.stdin.readline())
abs_list = list(map(int, sys.stdin.readline().split()))
maximum = 0

# 순열 함수 만들기
def permutation(array, n):
    size = len(array)
    visited = [False] * size

    def generate(chosen, visited):
        if len(chosen) == n:
            # print(chosen)
            max_result(chosen)
            return 
        
        for i in range(size):
            if not visited[i]:
                chosen.append(array[i])
                visited[i] = True
                generate(chosen, visited)
                visited[i] = False
                chosen.pop()

    generate([], visited)

# result 값 구하기
def max_result(chosen):
    global maximum
    result = 0
    for i in range(test_num - 1):
        result += abs(chosen[i] - chosen[i+1])
    if result > maximum:
        maximum = result

permutation(abs_list, test_num)
print(maximum)