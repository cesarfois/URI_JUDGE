import re
n = int(input())
for i in range(n):
    s = input()
    tnew = ''
    for e in s:
        if re.match("[a-zA-Z]", e):
            tnew = tnew + chr(ord(e)+3)
        else:
            tnew += e

    tnew = tnew[::-1]
    meio = int((len(tnew) / 2))
    metade1 = tnew[0:meio]
    metade2 = tnew[meio:]
    metade_new = ''

    for l in metade2:
        metade_new += chr(ord(l) - 1)

    tfinal = metade1 + metade_new

    print(tfinal)