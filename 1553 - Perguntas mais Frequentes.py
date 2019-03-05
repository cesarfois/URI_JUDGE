while True:
    try:
        n, k = map(int, input().split())
        if n == k == 0:
            break

        l = list(map(int, input().split()))
        res = 0
        l1 = set(l)
        for i in l1:
            if l.count(i) >= k:
                res += 1
        print(res)

    except EOFError:
        break
