import re

while True:
    try:

        s = input()

        simb = "\/'""<>?!@#$%^&*()_-+={}[] `´|/.,:;~"

        n = mi = ma = a = False

        for i in s:
            if i in simb:
                a = True
            if re.match("[a-z]", i):
                mi = True
            if re.match("[A-Z]", i):
                ma = True
            if re.match('[0-9]', i):
                n = True

        if len(s) < 6 or len(s) > 32:
            print('Senha invalida.')
        elif a is True:
            print('Senha invalida.')
        elif ma is True:
            if mi is True:
                if n is True:
                    print('Senha valida.')
        else:
            print('Senha invalida.')

    except EOFError:
        break
