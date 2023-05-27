from sys import stdin as s
s = open('input.txt', 'r')

n = int(s.readline().strip())
cards = list(map(int, s.readline().split()))
cards.sort()

m = int(s.readline().strip())
my_cards = list(map(int, s.readline().split()))

def find(num, start, end):
    while start <= end:
        half = (start + end) // 2
        if cards[half] == num:
            return half
        elif cards[half] > num:
            end = half - 1
        else:
            start =  half + 1
    return None

for i in range(m):
    if find(my_cards[i], 0, n - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')
print()