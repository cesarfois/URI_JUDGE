from operator import itemgetter
flag = False
while True:
    try:

        l = list(input())
        if l[0] == '':
            break
        if flag:
            print()
        flag = True

        d = {}
        lset = l.copy()
        lset = set(lset)
        lres = []

        for i in lset:
            d['ord'] = ord(i)
            d['contador'] = l.count(i)
            lres.append(d.copy())

        lres = sorted(lres, key=itemgetter('ord'), reverse=True)
        lres = sorted(lres, key=itemgetter('contador'))

        for i in lres:
            print(i['ord'], i['contador'])

    except EOFError:
        break
