# 2부터 N까지 모든 정수를 적는다.
# 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
# P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
# 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.

N, K = map(int, input().split())
initialList = list(range(2, N + 1))
primeNumList = []

while len(initialList) != 0:
    P = initialList[0]
    del initialList[0]
    K -= 1
    if K == 0:
        print(P)
        break
    temp = P
    while temp <= N:
        temp += P
        if temp in initialList:
            initialList.remove(temp)
            print(initialList)
            K -= 1
            if K == 0:
                print(temp)
                break
        
        

    primeNumList.append(P)
