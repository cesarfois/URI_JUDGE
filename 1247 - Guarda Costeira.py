while True:
    try:
        di, vf, vg = map(int, input().split())
        h = ((di*di) + (12*12)) ** (1/2)

        df = 12/vf
        dg = h/vg

        if dg <= df:
            print('S')
        else:
            print('N')
    except EOFError:
        break