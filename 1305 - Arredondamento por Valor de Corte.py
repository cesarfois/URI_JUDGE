while True:
    try:
        a = float(input())
        b = float(input())

        numb = float(a) - int(a)

        if numb >= b:
            print('%i' % (int(a) + 1))
        else:
            print('%i' % int(a))

    except EOFError:
        break