x, y, w, h = input().split(' ')
x = int(x)
y = int(y)
w = int(w)
h = int(h)
def shortestDistance(x, y, w, h):
    x0 = x - 0
    y0 = y - 0
    wx = w - x
    hy = h - y
    print(min(x0, y0, wx, hy))
shortestDistance(x, y, w, h)