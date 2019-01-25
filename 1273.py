first = True
while True:
    try:
        n = int(input())
        if n == 0:
            break
        l = []
        for i in range(n):
            s = input()
            l.append(s)

        m = max(l, key=len)
        if first == False:
            print()
        for i in range(len(l)):
            if l[i] == '':
                print('')
            else:
                print(l[i].rjust(len(m)))

        first = False

    except EOFError:
        break
