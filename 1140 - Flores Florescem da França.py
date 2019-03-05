while True:
    try:
        s = list(map(str,input().split()))
        if s[0] == '*':
            break

        temp = s[0][0].lower()
        c = 0
        for i in range(len(s)):
            s[i] = s[i].lower()
            if temp == s[i][0]:
                c += 1

        if c == len(s):
            print('Y')
        else:
            print('N')

    except EOFError:
        break
