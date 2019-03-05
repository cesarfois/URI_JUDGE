while True:
    try:
        s = input()

        for c in s:
            if ord(c) >= ord('a') and ord(c) <= ord('z'):
                if ord(c) + 13 > ord('z'):
                    print("%c" % (ord(c) - 13), end='')
                else:
                    print("%c" % (ord(c) + 13), end='')

            elif ord(c) >= ord('A') and ord(c) <= ord('Z'):
                if ord(c) + 13 > ord('Z'):
                    print("%c" %(ord(c) - 13), end='')
                else:
                    print("%c" % (ord(c) + 13), end='')

            else:
                print("%c" % c , end='')
        print()
    except EOFError:
        break