while True:
    try:
        s = ''
        l = list(input())
        n = int(input())
        letras = list(map(int,input().split()))

        for i in letras:
            s = s + l[i-1]
        print(s)
    except EOFError:
        break
