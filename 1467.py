while True:
    try:
        a,b,c = map(int,input().split())

        if a == b == c:
            print('*')
        elif a != b !=c:
            print('B')
        elif b != a != c:
            print('A')
        elif b != c != a:
            print('C')
    except EOFError:
        break



