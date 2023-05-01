from sys import stdin as s
s = open('input.txt', 'r')

test_num = int(s.readline().strip())

for _ in range(test_num):
    n = int(s.readline().strip())
    possible = n
    new_face = []
    for _ in range(n):
        new_face.append(list(map(int, s.readline().split())))
    new_face.sort()

    fail = set()
    first = new_face[0]
    for i in new_face:
        if i[0] > first[0] and i[1] > first[1]:
            fail.add(tuple(i))
        else:
            first = i

    new_face.sort(key=lambda x: x[1])
    first = new_face[0]
    for i in new_face:
        if i[0] > first[0] and i[1] > first[1]:
            fail.add(tuple(i))
        else:
            first = i
    print(n - len(fail))