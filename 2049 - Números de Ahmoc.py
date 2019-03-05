first = True
c = 0
while True:
    try:
        chave = str(input())
        if chave == '0':
            break
        ling = str(input())
        c += 1
        if first == False:
            print()
        if chave in ling:
            print('Instancia %d' % c)
            print('verdadeira')
        else:
            print('Instancia %d' % c)
            print('falsa')

        first = False
    except EOFError:
        break