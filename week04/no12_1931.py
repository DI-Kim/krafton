from sys import stdin as s
s = open('input.txt', 'r')

n = int(s.readline().strip())
time_table = []

for _ in range(n):
    time_table.append(list(map(int, s.readline().split())))

# 시작 시간 x[0] 을 정렬을 안해주면 반례가 생김
# 2    반례
# 3 3
# 2 3
time_table.sort(key = lambda x: (x[1], x[0]))
for i in time_table:
    print(i)
meeting = []


for i in time_table:
    if meeting:
        if meeting[-1][1] <= i[0]:
            meeting.append(i)
    else:
        meeting.append(i)
print(len(meeting))
