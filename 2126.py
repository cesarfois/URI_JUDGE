caso = 1
while True:
    try:
        res = 0
        pos = 0
        n = input()
        if n.isalpha():
            break
        n = list(n)
        linguica = list(input())

        for i in range(0, len(linguica)):
            if n == (linguica[i:len(n)+i]):
                res += 1
                pos = i + 1

        if res == 0:
            print('Caso #%d:\nNao existe subsequencia\n' % caso)
        else:
            print('Caso #%d:\nQtd.Subsequencias: %d\nPos: %d\n' % (caso, res, pos))
        caso += 1
    except EOFError:
        break