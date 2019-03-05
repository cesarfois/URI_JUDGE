res = 0
c = 0
while True:
    try:
        a = input()
        if a == '':
            print('%.1f' % (res / c))
            break
        if a == '.':
            print('%.1f' % (res / c))
            break
        b = int(input())
        if b == '':
            print('%.1f' % (res / c))
            break
        if a == '.':
            print('%.1f' % (res / c))
            break
        res += b
        c += 1

    except EOFError:
        print('%.1f' % (res / c))
        break