first = True
while True:
    try:
        n = int(input())
        if n == 0:
            break
        l = []
        s2, s1 = '', ''
        l1 = []
        for i in range(n):
            s1 = ''
            s = input().strip().split()
            for e in s:
                s1 += e + ' '
            l.append(s1)

        m = max(l, key=len)

        if first == False:
            print()
        for i in range(len(l)):
            s2 = l[i].rjust(len(m))
            print(s2[:-1])

        first = False
    except EOFError:
        break
