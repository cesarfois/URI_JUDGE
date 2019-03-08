while True:
    try:
        n = int(input())
        if n == '':
            break
        if n == 360 or 0 <= n < 90:
            print('Bom Dia!!')
        elif 90 <= n < 180:
            print('Boa Tarde!!')
        elif 180 <= n < 270:
            print('Boa Noite!!')
        elif 270 <= n < 360:
            print('De Madrugada!!')



    except EOFError:
        break