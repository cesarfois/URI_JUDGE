
n = int(input())
for i in range(n):

    x = float(input())
    d = 0

    while x > 1:
        x = x / 2.0
        d += 1

    print('%d dias' % d)