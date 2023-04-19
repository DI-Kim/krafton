import sys

def area(start, end):
    if start == end:
        return rec[start]
    else:
        mid = (start + end) // 2
        left_area = area(start, mid)
        right_area = area(mid + 1, end)
        max_area = max(left_area, right_area)

        x = mid
        y = mid + 1
        mid_min_height = min(rec[x], rec[y])
        width = 2
        mid_area = width * mid_min_height
        # x, y 포인터가 감소 및 증가하며 값을 찾음
        while start < x or end > y:
            if y == end or (start < x and rec[x - 1] >= rec[y + 1]):
                x -= 1
                width += 1
                mid_min_height = min(mid_min_height, rec[x])
                mid_area = max(mid_area, width * mid_min_height)
            elif x == start or y < end and rec[y + 1] >= rec[x-1]:
                y += 1
                width += 1
                mid_min_height = min(mid_min_height, rec[y])
                mid_area = max(mid_area, width * mid_min_height)
        max_area = max(max_area, mid_area)
        return max_area

while True:
    input_list = list(map(int, sys.stdin.readline().split()))
    if input_list == [0]:
        break
    N = input_list[0]
    rec = input_list[1:]

    print(area(0, N-1))