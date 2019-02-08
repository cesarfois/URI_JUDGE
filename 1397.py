while True:
    try:
        n = int(input())
        if n == 0:
            break
        c = c1 = 0
        for i in range(n):
            a, b = map(int, input().split())
            if a > b:
                c += 1
            elif b > a:
                c1 += 1
        print('{} {}'.format(c, c1))

    except EOFError:
        break