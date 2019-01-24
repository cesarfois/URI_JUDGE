while True:
    try:
        s = input()
        p = int(input())
        c, clock = 0, 0

        for i in range(len(s)):
            if s[i] == 'W':
                clock += 1
                if c > 0:
                    c = 0
                    clock += 1
            else:
                c += 1
                if c == p:
                    clock += 1
                    c = 0
        if c > 0:
            clock += 1

        print(clock)

    except EOFError:
        break