
while True:
    try:
        s = input()
        res = ''

        maiuscula = True

        for letra in s:
            if letra == ' ':
                res += ' '
            elif maiuscula:
                res += letra.upper()
                maiuscula = False
            else:
                res += letra.lower()
                maiuscula = True

        print(res)
    except EOFError:
        break




