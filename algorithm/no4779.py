from sys import stdin as s
s = open('input.txt', 'r')

while True:
    try:
        N = int(s.readline().strip())

        n = 3 ** N

        def cantoa(n):
            if n == 1:
                print("-", end='')
                return
            n //= 3
            cantoa(n)
            for i in range(n):
                print(' ', end='')
            cantoa(n)
        
        cantoa(n)
        print()

    except:
        break