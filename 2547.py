while True:
    try:

        n, amin, amax = map(int,input().split())
        c = 0

        for i in range(n):
            t = int(input())
            if t >= amin and t <= amax:
                c += 1
        print(c)
    except EOFError:
        break