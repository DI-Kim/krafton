caseNum = int(input())
result = ''

for i in range(caseNum):
    baseList = list(map(int, input().split()))
    num = baseList[0]
    grade = baseList[1:]

    avg = 0
    overAvg = 0

    for i in grade:
        avg += i

    avg = avg / num

    for i in grade:
        if i > avg:
            overAvg += 1
    over = f'{overAvg / num * 100:.3f}'
    result += over + "%\n"

result = result[:-1]
print(result)