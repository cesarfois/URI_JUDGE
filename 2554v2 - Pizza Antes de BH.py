
while True:
    try:
        p, d = map(int, input().split())
        reuniao = False
        res = ''
        l = []
        for _ in range(d):
            l = list(map(str,input().split()))
            s = l[1:]
            c = 0
            for e in s:
                if e == '1':
                    c += 1
            if c == p and not reuniao:
                res = l[0]
                reuniao = True

        if reuniao:
            print(res)
        else:
            print('Pizza antes de FdI')

    except EOFError:
        break


