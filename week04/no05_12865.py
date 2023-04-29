from sys import stdin as s
s = open('input.txt', 'r')

n, k = map(int, s.readline().split())
bag = [[0] * (k + 1) for _ in range(n + 1)]

luggage = [[0, 0]]
for _ in range(n):
    luggage.append(list(map(int, s.readline().split())))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w, v = luggage[i]
        

        if w > j:
            # 지금 들고있는 물건의 무게가 가방의 무게보다 무겁다면
            # 전의 물건이 들어있는 가방의 가치를 그대로 가져옴
            bag[i][j] = bag[i - 1][j]
        else: # 들고있는 물건의 무게가 가방의 무게보다 가볍다면
            # 가방의 무게에서 무게를 뺀 가방에 현재 물건의 가치를 더한 것과
            # 전의 물건이 들어있는 가방의 가치를 비교
            bag[i][j] = max(bag[i - 1][j - w] + v, bag[i - 1][j])

print(bag[-1][-1])