
string = input().split()

i = int(string[0])
f = int(string[1])

if f > i:
    t = f - i
    print("O JOGO DUROU %d HORA(S)" % t)
if i > f:
    t = (24 - i) + f
    print("O JOGO DUROU %d HORA(S)" % t)
if f == i:
    print("O JOGO DUROU 24 HORA(S)")


