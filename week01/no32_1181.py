import sys
testNum = int(sys.stdin.readline())
result = set()
for i in range(testNum):
    word = sys.stdin.readline().strip()
    result.add(word)

resultList = sorted(list(result))
resultList.sort(key=lambda x: len(x))

for i in resultList:
    print(i)