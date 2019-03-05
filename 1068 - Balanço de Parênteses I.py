while True:
    try:
        c1 = c = 0
        flag = True
        s = input()

        if s == '':
            flag = True
        elif s[0] == ')' or s[-1] == '(':
            flag = False

        c = s.count('(')
        c1 = s.count(')')

        if c == 0 and c1 == 0 and s == '':
            print('correct')
        elif c == 0 or c1 == 0 and s != 0:
            print('incorrect')
        elif c == 1 and c1 == 1:
            if flag is True:
                print('correct')
            else:
                print('incorrect')
        elif c == c1:
            if flag is True:
                print('correct')
            else:
                print('incorrect')
        else:
            print('incorrect')
    except EOFError:
        break
