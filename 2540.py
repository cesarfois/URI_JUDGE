while True:
    try:

        n = int(input())
        l = list(map(int, input().split()))

        if (2*n)/3 <= l.count(1):
            print('impeachment')
        else:
            print('acusacao arquivada')

    except EOFError:
        break