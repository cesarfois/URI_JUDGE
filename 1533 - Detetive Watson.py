while True:
    try:
        l = []
        l1 = []
        n = int(input())
        if n == 0:
            break
        l = list(map(int,input().split()))
        l1 = l.copy()
        l1.sort(reverse=True)

        print(l.index(l1[1]) + 1)

    except EOFError:
        break