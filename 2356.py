while True:
    try:
        d = input()
        if d == '':
            break

        s = input()

        if s in d:
            print('Resistente')
        else:
            print('Nao resistente')

    except EOFError:
        break