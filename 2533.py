while True:
    try:

        n = int(input())
        s = nom = den = 0
        for _ in range(n):
            a, b = map(int,input().split())

            nom += (a * b)
            s += b
        den = s * 100
        res = nom / den
        print('{:.4f}'.format(res))

    except EOFError:
        break