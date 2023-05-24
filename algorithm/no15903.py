import heapq
from sys import stdin as s
s = open('input.txt', 'r')

n, m = map(int, s.readline().split())

cards = list(map(int, s.readline().split()))

heapq.heapify(cards)

for _ in range(m):
    num1 = heapq.heappop(cards)
    num2 = heapq.heappop(cards)

    num = num1 + num2
    heapq.heappush(cards, num)
    heapq.heappush(cards, num)

print(sum(cards))