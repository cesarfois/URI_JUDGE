while True:
    try:

        n, t = map(int, input().split())
        res = 0
        for _ in range(n):
            a, b = map(int,input().split())
            if b == 0:
                if a == t:
                    res += 1
        print(res)

    except EOFError:
        break

