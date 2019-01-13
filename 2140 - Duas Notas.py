
while True:
    try:
        c, p = map(int, input().split())
        if c == 0 or p == 0:
            break
        notas = (2, 5, 10, 20, 50, 100.)
        troco = p - c
        existe = False

        for i in range(len(notas)):
            for j in range(len(notas)):
                if (notas[i] + notas[j]) == troco:
                    existe = True

        if (existe == True):
            print('possible')
        else:
            print('impossible')
    except EOFError:
        break
