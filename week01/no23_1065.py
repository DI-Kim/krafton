testNumStr = input()
testNum = int(testNumStr)
result = 0
# 1부터 돌면서 한수가 있는지 찾기
for i in range(1, testNum + 1):
    # 두번째 자리수까지는 무조건 등차수열
    if i < 100:
        result += 1
    # 각 자리수 구하기
    else:
        firstDigit = 0
        secondDigit = 0
        thirdDigit = 0
        for j in range(len(testNumStr)):
            if j == 0:
                firstDigit = i % 10
            elif j == 1:
                secondDigit = (i % 100) // 10
            elif j == 2:
                thirdDigit = i // 100
        if thirdDigit - secondDigit == secondDigit - firstDigit:
            result += 1

print(result)