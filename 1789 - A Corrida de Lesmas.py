
while True:
    try:
        n = int(input())
        lista = list(map(int,input().split()))
        m = max(lista)
        if m < 10:
            print('1')
        elif m >= 10 and m < 20:
            print('2')
        elif m >= 20:
            print('3')

    except EOFError:
        break



