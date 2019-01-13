
while True:
    try:
        m, d = map(int,input().split())

        qdm = ['0','31','29','31','30','31','30','31','31','30','31','30','31']

        someses = 0

        for i in range(m,12):
            someses = someses + int(qdm[i])
        if m == 12:
            if d > 25:
                print('Ja passou!')
            if d == 24:
                print('E vespera de natal!')
            if d == 25:
                print('E natal!')
            if d < 24:
                td = 25 - d
                print(td)

        else:
             td = (someses - d) + 25
             print('Faltam %d dias para o natal!' % td)

    except EOFError:
        break