while True:
    try:
        x, m = map(int,input().split())

        if x != 0 or m != 0:
            print(m*x)

    except EOFError:
        break