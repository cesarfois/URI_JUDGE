par = []
impar = []

for i in range(15):
    n = int(input())
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    if len(par) == 5:
        a = 0
        for e in par:
            print("par[%d] = %d" % (a, e))
            a += 1
        par = []

    if len(impar) == 5:
        a = 0
        for e in impar:
            print("impar[%d] = %d" % (a, e))
            a += 1
        impar = []

if len(impar) > 0:
    a = 0
    for e in impar:
        print("impar[%d] = %d" % (a, e))
        a += 1

if len(par) > 0:
    a = 0
    for e in par:
        print("par[%d] = %d" % (a, e))
        a += 1

