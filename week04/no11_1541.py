# 괄호를 이용한 최소값 찾기
# + 를 무조건 먼저 더하고 -를 마지막에 계산
from sys import stdin as s
s = open('input.txt', 'r')

operator = []
operand = []

string = s.readline().strip()
temp = ''
for i in string:
    if i == '+':
        operator.append('+')
        operand.append(int(temp))
        temp = ''
    elif i == '-':
        operator.append('-')
        operand.append(int(temp))
        temp = ''
    else:
        temp += i
operand.append(int(temp))

for i in range(len(operator) - 1, -1, -1):
    if operator[i] == '+':
        operand[i] += operand[i + 1]
        del operand[i + 1]
        del operator[i]

result = operand[0]
for i in range(1, len(operand)):
    result -= operand[i]
print(result)