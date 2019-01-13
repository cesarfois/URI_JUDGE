
while True:
    try:
        a,b= map(int,input().split(':'))

        if a >= 7:
            atraso = ((a - 7) * 60) + b
        else:
            atraso = 0
    except EOFError:
        break
    print('Atraso maximo: %d' % atraso)

