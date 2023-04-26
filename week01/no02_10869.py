def cal(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(int(a / b))
    print(a % b)

a, b = input().split(' ')
cal(int(a), int(b))