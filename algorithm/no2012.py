from sys import stdin as s
s = open('input.txt', 'r')
n = int(s.readline().strip())
real_grade = []
for _ in range(n):
    real_grade.append(int(s.readline().strip()))

real_grade.sort()
grade = [i+1 for i in range(n)]
result = 0
for i in range(n):
    result += abs(real_grade[i] - grade[i])
print(result)