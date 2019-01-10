
while True:
    try:
        n = int(input())
        if n == 0:
            break
        t = {'suco de laranja': 120,
             'morango fresco':85,
             'mamao':85 ,
             'goiaba vermelha':70,
             'manga':56,
             'laranja': 50,
             'brocolis':34
             }
        soma = 0

        for i in range(n):
            a, b = map(str,input().split(' ',1))
            b = t[b]
            a = int(a)
            soma = (a * b) + soma

        if soma >= 130:
            print('Menos %d mg' % (soma - 130))
        elif soma <= 110:
            print('Mais %d mg' %(110 - soma))
        else:
            print('%d mg' % soma)
    except EOFError:
        break

