while True:
    try:
        h, cons = map(int,input().split())
        l1 = []
        l = []
        for i in range(h):
            l.append(int(input()))

        l.sort(reverse=True)
        for e in range(cons):
            l1.append(int(input()))

        for w in l1:
            print(l[w - 1])

    except EOFError:
        break