caseNum = int(input())
inputList = []

for _ in range(caseNum):
    num = int(input())
    inputList.append(num)
inputList.sort()

for i in inputList:
    print(i)