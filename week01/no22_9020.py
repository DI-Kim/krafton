caseNum = int(input())
initialList = list(range(2, 10001))
primeNumList = []
result = []

# 10000까지 소수를 리스트에 저장
while len(initialList) != 0:
    P = initialList[0]
    del initialList[0]
    primeNumList.append(P)
    temp = P
    while temp <= 10000:
        temp += P
        if temp in initialList:
            initialList.remove(temp)

# 최소 차이 골드바흐 파티션 찾기
for _ in range(caseNum):
    inputNum = int(input())
    i = inputNum // 2
    while True:
        if i in primeNumList and (inputNum - i) in primeNumList:
            print(i, inputNum - i)
            break
        else:
            i -= 1
