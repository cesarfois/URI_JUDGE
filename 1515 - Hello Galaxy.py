while True:
    try:
        n = int(input())
        if n == 0:
            break
        menor = 2200
        for i in range(n):
            a,b,c = map(str,input().split())
            b = int(b)
            if b - int(c) < menor :
                menor = b - int(c)
                res = a
        print(res)
    except EOFError:
        break