while True:
    try:
        d = {'W': 1,'H': 1/2,'Q': 1/4,'E': 1/8,'S': 1/16,'T': 1/32,'X': 1/64,}
        c = res = 0
        l = list(map(str,input().split('/')))
        if l[0] == '*':
            break

        for i in l:
            if c == 1:
                res += 1
            c = 0
            for w in i:
                c = c + d[w]
        print(res)
    except EOFError:
        break