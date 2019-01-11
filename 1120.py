while True:
    try:
        a , b = map(str,input().split())
        if int(a) == 0 and int(b) == 0:
            break

        b = b.replace(a,'')
        if b == '':
            b = int(0)
        if int(b) == 0:
            print(int(0))
        else:
            print(int(b))
    except EOFError:
        break
