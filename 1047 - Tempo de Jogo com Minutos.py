string = input().split()

i = int(string[0])
f = int(string[2])
mi = int(string[1])
mf = int(string[3])


if (f == i) & (mf == mi):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    if f > i:
        h = f - i
    if i > f:
        h = (24 - i) + f
    if mf > mi:
        m = mf - mi
    if mi > mf:
        m = (60 - mi) + mf
        h -= 1
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (h, m))