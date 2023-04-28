n, k = 25, 5  # count = 2
count = 0

while True:
    if n == 1:
        print(count)
        break
    if n % k == 0:
        n //= k
        count += 1
    else:
        n -= k
        count += 1