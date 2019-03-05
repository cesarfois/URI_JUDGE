while True:
    try:
        n = int(input())
        l = []
        for i in range(n):
            l.append(input())

        l = sorted(l)
        for i in l:
            print(i)

    except EOFError:
        break