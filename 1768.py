
while True:
    try:
        n = int(input())
        l = []
        s = ''

        for e in range(1,n+1,2):
            s = '{0:^{x}}'.format('*'*e, x=n)
            s = s.rstrip()
            print(s)

        for j in range(1,4,2):
            s = '{0:^{x}}'.format('*' *j, x=n)
            s = s.rstrip()
            print(s)
        print()

    except EOFError:
        break