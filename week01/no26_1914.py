def hanoi(n, base, moveTo):
    another = 6 - base - moveTo
    if n == 1:
        print(base, moveTo)
    else:
        hanoi(n-1, base, another)
        print(base, moveTo)
        hanoi(n-1, another, moveTo)

inputNum = int(input())

K = 2 ** inputNum - 1
print(K)
if inputNum <= 20:
    hanoi(inputNum, 1, 3)