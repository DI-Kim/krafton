a, b, c = int(input()), int(input()), int(input())

multiply = str(a * b * c)

result = [0 for _ in range(10)]

for i in multiply:
    for j in range(10):
        if int(i) == j:
            result[j] = result[j] + 1

for i in result:
    print(i)