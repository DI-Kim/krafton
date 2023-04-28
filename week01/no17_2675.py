for _ in range(int(input())):
    values = input().split()
        
    R = int(values[0])
    S = values[1]

    P = ''
    for i in S:
        for j in range(R):
            P += i
    print(P)