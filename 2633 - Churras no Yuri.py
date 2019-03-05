while True:
    try:

        n = int(input())
        la = []
        lb = []
        s = ''
        for i in range(n):
            a, b = map(str,input().split())
            la.append(a)
            la.append(int(b))
            lb.append(int(b))
        lb.sort()

        for e in lb:
            w = la.index(e)
            s += la[w-1] + ' '

        print(s[:-1])

    except EOFError:
        break