n = int(input())

for _ in range(n):
        d = sorted(set(input()))
        sc = sorted(set(input()))
        sa = sorted(set(input()))
        st = sc + sa

        sd = ''.join(d)
        sst = ''.join(st)
        res = ''
        comeucerto = True

        for i in sst:
            if i not in sd:
                comeucerto = False

        for w in sd:
            if w not in sst:
                res += w
        for f in sc:
            if f in sa:
                comeucerto = False

        if not comeucerto:
            print('CHEATER')
        else:
            print(res)


