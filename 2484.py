while True:
    try:
        s = input()
        if s == '':
            break
        s1 = ''
        s2 = ''
        for i in s:
            s1 += i + ' '
        s1 = s1.rstrip()
        n = len(s1)
        for e in range( n , 0, -2):
            s2 = ('{0:^{x}}'.format(s1[:e], x=n))
            s2 = s2.rstrip()
            print(s2)
        print()

    except EOFError:
        break