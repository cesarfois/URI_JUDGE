
while True:
    try:
        s = input()
        if s == '':
            break
        s1 = input()
        c = 0

        for i in s:
            for j in s1:
                if i == j:
                    c += 1
        print(c)

    except EOFError:
        break