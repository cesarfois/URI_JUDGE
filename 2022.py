from operator import itemgetter

while True:
    try:
        nome, n = input().split()
        n = int(n)
        l = []


        for i in range(n):
            gift = []
            gift.append(input())
            x, y = map(float, input().split())
            gift.append(x)
            gift.append(int(y))
            l.append(gift)

        l = sorted(l, key=itemgetter(0))
        l = sorted(l, key=itemgetter(1))
        l = sorted(l, key=itemgetter(2), reverse=True)

        print('Lista de %s' % nome)

        for i in l:
            print('%s - R$%.2f' % (i[0], i[1]))
        print()


    except EOFError:
        break
