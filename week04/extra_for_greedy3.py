# n, m = 3, 3
# cards = [[3, 1, 2], [4, 1, 4], [2, 2, 2]]
n, m = 2, 4
cards = [[7, 3, 1, 8], [3, 3, 3, 4]]
result = 0

for i in cards:
    min_value = 100000
    for j in i:
        if j < min_value:
            min_value = j
    if min_value > result:
        result = min_value

print(result)

