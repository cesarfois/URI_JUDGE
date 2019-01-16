while True:
    try:

        a, b = map(int, input().split())
        res = b - a
        print(abs(res))

    except EOFError:
        break