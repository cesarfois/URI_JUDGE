
l1 = []
while True:
    try:
        res = ''
        l = []
        l = list(map(str,input().split()))
        if l[0] == '0':
            l1 = sorted(l1, key=str.upper)
            print()
            print('The biggest word: %s' % (max(l1, key=len)))
            break
        l1 += l
        for i in l:
            res += str(len(i)) + '-'
        print(res.rstrip('-'))

    except EOFError:
        break