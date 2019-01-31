while True:
    try:
        n = int(input())
        if n == 0:
            break
        res = 0
        s = ''
        i = 1

        while res < n:
            res = i * i
            i += 1
            if res <= n:
                s += str(res) + ' '
        print(s[:-1])

    except EOFError:
        break