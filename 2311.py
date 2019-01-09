n = int(input())

for i in range(n):
    l = []
    nome = input()
    dif = float(input())
    l = list(map(float, input().split(' ')))

    l = sorted(l, key=float)
    del l[0]
    del l[-1]

    print('%s %.2f' % (nome, (sum(l) * dif)))