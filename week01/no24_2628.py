width, height = map(int, input().split())
tryNum = int(input())
widthList = [0]
heightList = [0]

for i in range(tryNum):
    guide, cutNum = map(int, input().split())
    if guide == 0:
        heightList.append(cutNum)
    elif guide == 1:
        widthList.append(cutNum)

heightList.sort()
heightList.append(height)
widthList.sort()
widthList.append(width)
maxValue = 0
maxWidth = 0
maxHeight = 0

for w1, w2 in zip(widthList, widthList[1:]):
    if w2 - w1 > maxValue:
        maxValue = w2 - w1
maxWidth = maxValue
maxValue = 0

for h1, h2 in zip(heightList, heightList[1:]):
    if h2 - h1 > maxValue:
        maxValue = h2 - h1
maxHeight = maxValue

print(maxWidth * maxHeight)