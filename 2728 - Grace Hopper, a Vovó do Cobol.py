while True:
    try:
        l = input().lower().split('-')
        if l[0] == '':
            break
        c = 0
        s1 = 'cobol'
        for i in range(len(s1)):
            if s1[i] in l[i][:1] or s1[i] in l[i][-1]:
                c += 1
        if c == 5:
            print('GRACE HOPPER')
        else:
            print('BUG')

    except EOFError:
        break