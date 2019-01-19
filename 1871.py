while True:
    try:

        a, b = map(int, input().split())
        if a == 0 == b:
            break

        c = str(a+b)
        c = c.replace('0','')

        print(c)

    except EOFError:
        break

