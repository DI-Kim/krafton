listLen, standardNum = map(int, input().split())
inputNums = list(map(int, input().split()))
str = ''

if len(inputNums) > listLen:
    inputNums = list(map(int, input().split()))


for i in inputNums:
    if standardNum > i:
        str += f'{i} '
str = str[0:-1]
print(str)