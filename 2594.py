

n = int(input())

for w in range(n):
    s = input()
    f = input()

    res = []
    res1 = ''

    if s == f:
        res.append(0)
    elif s.startswith(f + ' '):
        res.append(0)

    fspace = ' ' + f + ' '
    i = 0
    while i != -1:
        i = s.find(fspace, i + 1)
        if i != -1:
            res.append(i + 1)
    if s.endswith(' ' + f):
        res.append(len(s) - (len(f)))

    for i in res:
        res1 += str(i) + ' '
    if len(res) > 0:
        print(res1[:-1])
    else:
        print(-1)
