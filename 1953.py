while True:
    try:
        n = int(input())

        p = 0
        h = 0
        intru = 0

        for i in range(n):
            a, b =  map(str, input().split())
            if b == 'EPR':
                p += 1
            elif b == 'EHD':
                h += 1
            else:
                intru += 1

        print('EPR: %d' %p)
        print('EHD: %d' %h)
        print('INTRUSOS: %d' %intru)

    except EOFError:
        break