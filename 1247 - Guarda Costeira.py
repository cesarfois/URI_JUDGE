ERRRADA ==
while True:
    try:
        di, vf, vg = map(int, input().split())
        df = vf + di
        dg = vg
        pegou = "N"
        while df <= 12:
            if dg >= df:
                pegou = "S"
                break
            dg += vg
            df += vf
        print(pegou)

    except EOFError:
        break


