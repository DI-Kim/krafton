answer = input().split()
firstNum = int(answer[0][2] + answer[0][1] + answer[0][0])
secondNum = int(answer[1][2] + answer[1][1] + answer[1][0])
if firstNum > secondNum:
    print(firstNum)
else:
    print(secondNum)