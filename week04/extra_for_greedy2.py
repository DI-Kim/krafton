# n: 배열의 크기, m: 더해지는 횟수, k: 반복 가능 횟수
n, m, k = 5, 8, 3
input_list = [2, 4, 5, 4, 6]

input_list.sort()

biggest = input_list[-1]
bigger = input_list[-2]

# 수학적 풀이
result = 0
count = m // (k + 1)

result += (count * bigger)
result += ((m - count) * biggest)
print(result)

# for 문 이용
result = 0
while True:
    for _ in range(k):
        if m == 0:
            break
        result += biggest
        m -= 1
    if m == 0:
        break
    result += bigger
    m -= 1
print(result)
