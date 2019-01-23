
while True:
    try:
        s = str(input())

        res = ''
        c = 0
        for i in s:
            if i == '_' and c == 1:
                res += '</i>'
                c = 0
            elif i == '_' and c != 1:
                res += '<i>'
                c = 1
            elif i == '*' and c == 1:
                res += '</b>'
                c = 0
            elif i == '*' and c != 1:
                res += '<b>'
                c = 1
            else:
                res += i

        print(res)
    except EOFError:
        break