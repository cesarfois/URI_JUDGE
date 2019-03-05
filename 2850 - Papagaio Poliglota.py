while True:
    try:

        s = str(input())
        if s == "":
            break

        if s == "esquerda":
            print('ingles')
        elif s == "direita":
            print('frances')
        elif s == 'as duas':
            print('caiu')
        else:
            print('portugues')


    except EOFError:
        break
