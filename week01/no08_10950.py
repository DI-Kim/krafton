caseNum = int(input())
inputList = []

for i in range(caseNum):
    a, b = map(int, input().split())
    inputList.append([a, b])

for i in inputList:
    print(i[0] + i[1])