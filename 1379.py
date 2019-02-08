while True:
    try:
        c = 0.0
        a, b = map(int,input().split())
        if a == 0 == b:
            break
        c = 2*a - b
        print(c)

    except EOFError:
        break