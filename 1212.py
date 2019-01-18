while True:
    try:
        s , s1 = map(int,input().split())
        if s == 0 and s1 == 0:
            break
        carry, c, w = 0, 0, 0

        while w < 9:
            a = int(s) % 10
            b = int(s1) % 10
            s = s / 10
            s1 = s1 / 10
            if (a + b + carry) >= 10:
                carry = 1
                c += 1
            else:
                carry = 0
            w += 1

        if c == 0:
            print('No carry operation.')
        elif c == 1:
            print('1 carry operation.')
        else:
            print('%d carry operations.' % c)
    except EOFError:
        break