maxNum = 0
for i in range(9):
    a = int(input())
    if a > maxNum:
        maxNum = a
        indexNum = i + 1
print(maxNum)
print(indexNum)