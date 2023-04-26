result = 0

N = int(input())
listNum = list(map(int, input().split()))
if len(listNum) == N:
    
    for i in listNum:
        if i == 1:
            continue
        result += 1
        for j in range(2, i):
            if i % j == 0:
                result -= 1
                break
    print(result)