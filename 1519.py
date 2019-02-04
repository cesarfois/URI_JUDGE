wrong 25%


while True:
    try:

        l = list(map(str,input().split()))
        if l[0] == '.':
            break

        menor = min(sorted(l), key=len)

        l1 = l.copy()
        l1 = sorted(l1, key=len)
        while l1.count(menor) >= 1 and len(l1) < 1:
            while menor in l1:
                l1.remove(menor)
            menor = min(sorted(l1), key=len)

        res = ''
        elem = 0
        c = 0


        for i in l:
            if i != menor:
                res += i[0] + '. '
            else:
                res += i + ' '

        print(res.rstrip())


        for i in l:
            if i != menor:
                elem += 1
        print(elem)

        l= sorted(l)
        for i in l:
            if i != menor:
                print(i[0]+'. = ' + i)

    except EOFError:
        break