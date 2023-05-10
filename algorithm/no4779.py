from sys import stdin as s
s = open('input.txt', 'r')

while True:
    try:
        N = int(s.readline().strip())

        n = 3 ** N

        def cantor(n):
            if n == 1:
                print("-", end='')
                return
            n //= 3

            cantor(n)
            
            for i in range(n):
                print(' ', end='')
            
            cantor(n)
        
        cantor(n)
        print()

    except:
        break