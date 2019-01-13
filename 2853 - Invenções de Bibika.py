while True:
    try:
        l = []
        res = 0
        n = int(input())
        for i in range(n):
            d = float(input())
            if d <= 2 or d >= 99:
                break
            if d >= 9.0 and d <= 11.0:
                l.append(d)
                res = min(l)

        print('%.2f' %res)

    except EOFError:
        break