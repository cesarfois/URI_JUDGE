n = int(input())
p = ['0.30', '0.59', '0.11']
l = []
c = 0
for _ in range(n):
    res = 0
    conv = input()
    l = list(map(int, input().split()))

    if conv == 'min':
        res = min(l)
    elif conv == 'max':
        res = max(l)
    elif conv == 'mean':
        res = sum(l)/len(l)
    elif conv == 'eye':
        for i in range(len(p)):
            res += l[i] * float(p[i])
    c += 1
    print('Caso #%d: %d' % (c, res))


