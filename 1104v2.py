while True:
    try:
        a, b = map(int, input().split())
        if a == b == 0:
            break
        la = set(list(map(int,input().split())))
        lb = set(list(map(int,input().split())))
        c = 0

        if len(la) >= len(lb):
            for i in lb:
                if i not in la:
                    c += 1
        else:
            for i in la:
                if i not in lb:
                    c += 1
        print(c)
    except EOFError:
        break