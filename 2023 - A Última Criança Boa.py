while True:
    try:
        l = []
        while True:
            try:
                s = input()
                if s != '':
                    l.append(s)
                else:
                    break
            except EOFError:
                break

        l = sorted(l, key=str.lower)
        print(l[-1])
        break
    except EOFError:
        break