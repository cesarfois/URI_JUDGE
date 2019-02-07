while True:
    try:
        l = []
        while True:
            a = input()
            if len(a) == 0:
                break
            l.append(a)
        print(l)
    except EOFError:
        break

