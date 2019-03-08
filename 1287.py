import re
while True:
    try:
        s = input()
        res = ''
        maior = False
        aux = 0


        for i in s:
            if i != ' ' and i != ',':
                if re.match('[0-9]', i):
                    res += i
                elif i == 'o':
                    res += '0'
                elif i == 'O':
                    res += '0'
                elif i == 'l':
                    res += '1'
                elif re.match('[a-z A-Z]', i):
                    res += i
                else:
                    res += i


        if res.isdigit():
            aux = int(res)
            if int(aux) >= 2147483647:
                if len(res) > 10:
                    maior = True

            if aux > 2147483647:
                maior = True

        if res.isdigit() and not maior :
                print('%d' % int(res))
        else:
            print('error')

    except EOFError:
        break
