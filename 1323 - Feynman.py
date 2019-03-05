while True:
    try:
        n = int(input())
        if n == 0:
            break
        ans = (n * (n + 1)) * (2 * n + 1)
        t = ans / 6

        print('%d' % t)

    except EOFError:
        break