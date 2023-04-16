# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때,
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
import sys

def binary_search(value, start, end):
    mid = (start + end) // 2
    if start == end:
        if A[mid-1] == value:
            print(1)
        else:
            print(0)
        return
    if A[mid] == value:
        print(1)
    elif A[mid] < value:
        binary_search(value, mid+1, end)
    elif A[mid] > value:
        binary_search(value, start, mid)



N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
M = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().split()))

for i in input_list:
    binary_search(i, 0, len(A))
    