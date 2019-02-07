
while True:
    try:
        p, d = map(int, input().split())

        l = []
        l1 = []
        for _ in range(d):
            s = input()
            l.append(s)
        for i in l:
            c = 0
            for e in i[9:]:
                if e == '1':
                    c += 1
            if c == p:
                l1.append(i)

        if len(l1) >= 1:
            res = l1[0][:10]
            res = res.rstrip(' 1')
            res = res.rstrip()
            print(res)
        else:
            print('Pizza antes de FdI')

    except EOFError:
        break


