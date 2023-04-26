import sys

test_num = int(sys.stdin.readline())
# 10000 아하의 자연수만 받으므로, 빈리스트를
# 입력받는 숫자에 대한 횟수를 업데이트 해줌
# 입력받는 숫자 = 인덱스 + 1
empty_list = [0] * 10000

for _ in range(test_num):
    input_num = int(sys.stdin.readline())
    empty_list[input_num - 1] += 1

for i in range(len(empty_list)):
    if empty_list[i] != 0:
        for j in range(empty_list[i]):
            print(i + 1)