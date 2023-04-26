# 외판원 순회 2
import sys

def search(start, cur, city_num, distance):
    global result
    # 도시 넘버가 N과 같으면 순회 끝, 마지막 시작도시로 가는 값 더해주기
    if city_num == N:
        if input_list[cur][start]:
            distance += input_list[cur][start]
            if result > distance:
                result = distance
        return
    
    # 도시 순회
    for i in range(N):
        if not visited[i] and input_list[cur][i] != 0:
            visited[i] = True
            # distance += input_list[cur][i]
            search(start, i, city_num + 1, distance + input_list[cur][i])
            visited[i] = False

N = int(sys.stdin.readline())
visited = [False] * N
result = 1000000 * N
input_list = []
for _ in range(N):
    input_list.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    visited[i] = True
    search(i, i, 1, 0)
    visited[i] = False

print(result)
