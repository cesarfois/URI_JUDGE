# so funcionou no python 2

n = int(input())
inst = 0
for i in range(n):

    frasecerta = raw_input()
    frase1 = raw_input()
    frase2 = raw_input()
    c1 = c2 = 0
    p = False
    win = ''
    l = frasecerta, frase2 , frase1
    d = min(l, key=len)

    for i in range(len(d)):
        if frasecerta[i] == frase1[i]:
            c1 += 1
        if frasecerta[i] == frase2[i]:
            c2 += 1
        if frasecerta[i] == frase1[i] and p == False:
            if frasecerta[i] != frase2[i]:
                win = '1'
                p = True
        if frasecerta[i] == frase2[i] and p == False:
            if frasecerta[i] != frase1[i]:
                win = '2'
                p = True
    inst += 1
    if c2 > c1 or c1 == c2 and win == '2':
        print('Instancia %d' % inst)
        print('time 2\n')
    elif c2 < c1 or c1 == c2 and win == '1':
        print('Instancia %d' % inst)
        print('time 1\n')
    elif c1 == c2:
        print('Instancia %d' % inst)
        print('empate\n')
