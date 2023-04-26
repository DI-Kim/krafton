import sys
# brute force
# 입력 받은 키를 리스트로 저장
def findDwarf():
    height_list = []
    for _ in range(9):
        height_list.append(int(sys.stdin.readline().strip()))
    sum = 100
    for first in range(3):
        for second in range(1, 4):
            if height_list[first] == height_list[second]:
                continue
            for third in range(2, 5):
                if height_list[second] == height_list[third] or height_list[first] == height_list[third]:
                    continue
                for fourth in range(3, 6):
                    if height_list[fourth] == height_list[third] or height_list[second] == height_list[fourth]:
                        continue
                    for fifth in range(4, 7):
                        if height_list[fifth] == height_list[third] or height_list[fifth] == height_list[fourth]:
                            continue
                        for sixth in range(5, 8):
                            if height_list[sixth] == height_list[fourth] or height_list[sixth] == height_list[fifth]:
                                continue
                            for seventh in range(6, 9):
                                if height_list[seventh] == height_list[sixth] or height_list[seventh] == height_list[fifth]:
                                    continue
                                if sum == height_list[first] + height_list[second] + height_list[third] + height_list[fourth] + height_list[fifth] + height_list[sixth] + height_list[seventh]:
                                    return height_list[first], height_list[second], height_list[third], height_list[fourth], height_list[fifth], height_list[sixth], height_list[seventh]

result = findDwarf()
if result is not None:
    result_list = list(result)
    result_list.sort()
    for i in result_list:
        print(i)