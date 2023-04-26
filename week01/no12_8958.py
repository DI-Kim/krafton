caseNum = int(input())
str = ''
for i in range(caseNum):
    oxResult = input()
    score = 0
    total = 0
    for i in range(len(oxResult)):
        if oxResult[i] == 'O':
            score += 1
            total += score
        else:
            score = 0
    str += f'{total}\n'
str = str[:-1]
print(str)