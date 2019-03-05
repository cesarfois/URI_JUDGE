while True:
    try:

        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        l = list(map(int,input().split()))
        l1 = l.copy()
        l1 = set(l1)
        res = 0

        for i in l1:
            if i in l:
               if l.count(i) >= 2:
                   res += 1
        print(res)

    except EOFError:
        break
