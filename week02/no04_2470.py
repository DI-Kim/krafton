# hint
# 투 포인터: 리스트에 순차적으로 접근해야 할 때 두개의 점의 위치를 기록하면서 처리하는 방식
import sys

n = int(sys.stdin.readline())
solutions = list(map(int, sys.stdin.readline().split()))
solutions.sort()

start = 0
end = n - 1
solution1 = solutions[start]
solution2 = solutions[end]
result = 2000000000

while start < end:
    value = abs(solutions[start] + solutions[end])
    if value <= result:
        result = value
        solution1 = solutions[start]
        solution2 = solutions[end]
    
    if value == 0:
        break
    if solutions[start] + solutions[end] < 0:
        start += 1
    elif solutions[start] + solutions[end] > 0:
        end -= 1
        
            

print(solution1, solution2)
