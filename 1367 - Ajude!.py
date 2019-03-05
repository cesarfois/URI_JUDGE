while True:
    try:
        n = int(input())
        if n == 0:
            break

        p = c = 0
        l = r1 = []
        for i in range(n):
            l = list(map(str, input().split()))
            if l[2] == 'incorrect':
                r1.append(l[0])
            if l[2] == 'correct':
                p += int(l[1])
                c += 1
                for e in r1:
                    if e == l[0]:
                        p += 20
        print(c, p)

    except EOFError:
        break


