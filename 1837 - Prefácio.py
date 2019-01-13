
a, b = map(int, input().split())

while b != 0:
    r = a % b
    q = a / b

    if r > 0:
        if q < 0:
            q -= 1
        if q > 0:
            q = q

    if r < 0:
        if q < 0:
            a += 1
            r = a - (b * q)
        if q > 0:
            q += 1

            r = a - (b*int(q))

    print("%d %d" % (q, abs(r)))

    break





