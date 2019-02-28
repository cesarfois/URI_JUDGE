while True:
    try:
        n = int(input())
        if n == 0:
            break
        l = []
        l1 = []
        res = 0
        for i in range(1, n+1):
            l.append(i)
        while True:
            try:
                l1 = list(map(int, input().split()))
                res += 1
                if l == l1:
                    print(res)
                    break

            except EOFError:
                break

    except EOFError:
        break

