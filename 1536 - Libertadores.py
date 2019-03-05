n = int(input())
for i in range(n):
    tgt1 = 0
    tgt2 = 0
    t1pontos = 0
    t2pontos = 0
    golsforat1 = 0
    golsforat2 = 0
    res = ''
    # partida 1
    t1, o, t2 = map(str, input().split())
    t1 = int(t1)
    t2 = int(t2)
    tgt1 += t1
    tgt2 += t2
    golsforat2 = t2
    if t1 > t2:
        t1pontos += 3
    elif t2 > t1:
        t2pontos += 3
    elif t1 == t2:
        t2pontos += 1
        t1pontos += 1
    # partida 2
    t2, o, t1 = map(str, input().split())
    t1 = int(t1)
    t2 = int(t2)
    tgt1 += t1
    tgt2 += t2
    golsforat1 = t1
    if t1 > t2:
        t1pontos += 3
    elif t2 > t1:
        t2pontos += 3
    elif t1 == t2:
        t2pontos += 1
        t1pontos += 1

    if t1pontos > t2pontos:
        res = 'Time 1'
    elif t2pontos > t1pontos:
        res = 'Time 2'
    else:
        if tgt1 > tgt2:
            res = 'Time 1'
        elif tgt2 > tgt1:
            res = "Time 2"
        else:
            if golsforat1 > golsforat2:
                res = 'Time 1'
            elif golsforat2 > golsforat1:
                res = 'Time 2'
            else:
                res = 'Penaltis'

    print(res)