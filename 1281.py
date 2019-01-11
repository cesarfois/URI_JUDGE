

n = int(input())
for i in range(n):
    res = 0
    preco, qde = [], []
    npreco = int(input())
    for i in range(npreco):
        a, b = map(str, input().split())
        preco.append(a)
        preco.append(float(b))

    nqde = int(input())

    for i in range(nqde):
        a, b = map(str, input().split())
        qde.append(a)
        qde.append(float(b))
        c = preco.index(a)
        res = res + (float(b) * float(preco[c+1]))

    print('R$ %.2f' % res)