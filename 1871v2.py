Wrong 15%

while True:
    try:

        a, b = map(int, input().split())
        if a == 0 == b:
            break

        c = str(a+b)
        res = ''

        for i in c:
            res += i
            if i == '0':
                res += ""

        print(res)

    except EOFError:
        break

