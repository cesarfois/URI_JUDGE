while True:
    try:
        l, r = map(int,input().split())
        if l == 0 == r:
            break
        print(l+r)
    except EOFError:
        break