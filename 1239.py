
while True:
    try:
        s = str(input())
        res = ''
        c, c1= 0, 0
        for i in s:
            if i == '_' and c % 2 == 0:
                res += '<i>'
                c += 1
            elif i == '_' and c % 2 != 0:
                res += '</i>'
                c += 1
            elif i == '*' and c1 % 2 == 0:
                res += '<b>'
                c1 += 1
            elif i == '*' and c1 % 2 != 0:
                res += '</b>'
                c1 += 1
            else:
                res += i

        print(res)
    except EOFError:
        break