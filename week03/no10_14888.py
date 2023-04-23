from sys import stdin as s
s = open('../input.txt', 'r')

N = int(s.readline().strip())

input_num = list(map(int, s.readline().split()))
# + - * //
operator = list(map(int, s.readline().split()))
min_result = 10 ** 9
max_result = -10 ** 9

def dfs(n, result, plus, sub, multiply, divide):
    global min_result, max_result
    if n == N:
        min_result = min(min_result, result)
        max_result = max(max_result, result)
        return
    
    if plus != 0:
        # operator[0] = operator[0] - 1
        # dfs(n + 1, result + input_num[n], operator)
        dfs(n + 1, result + input_num[n], plus - 1, sub, multiply, divide)
    if sub != 0:
        # operator[1] = operator[1] - 1
        # dfs(n + 1, result - input_num[n], operator)
        dfs(n + 1, result - input_num[n], plus, sub - 1, multiply, divide)
    if multiply != 0:
        # operator[2] = operator[2] - 1
        # dfs(n + 1, result * input_num[n], operator)
        dfs(n + 1, result * input_num[n], plus, sub, multiply - 1, divide)
    if divide != 0:
        # operator[3] = operator[3] - 1
        # dfs(n + 1, result // input_num[n], operator)
        if result < 0:
            result = ((-result) // input_num[n]) * -1
        else:
            result = result // input_num[n]
        
        dfs(n + 1, result, plus, sub, multiply, divide - 1)

dfs(1, input_num[0], operator[0], operator[1], operator[2], operator[3])
print(max_result)
print(min_result)