caso = 1
while True:
    try:
        n = int(input())
        c = 0
        c1 = 0
        restr = "0 "
        if n == 1:
            print('Caso %d: 2 numeros\n0 1\n' % caso)

        else:
            while n >= c and n != 1:
                qde = c
                for i in range(qde):
                    restr = restr + str(c) + ' '

                    c1 += 1
                c += 1
            if n != 0:
                print('Caso %d: %d numeros\n%s\n'% (caso, (c1+1), restr[:-1]))
            else:
                print('Caso %d: %d numero\n%s\n' % (caso, (c1 + 1), restr[:-1]))
        caso += 1
    except EOFError:
        break