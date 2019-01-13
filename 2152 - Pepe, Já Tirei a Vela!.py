n = int(input())



for i in range(n):
    h, m, o = map(int, input().split())
    if o == 1:
        o = 'A porta abriu!'
    else:
        o = 'A porta fechou!'

    print('%02i:%02i - %s' % (h, m, o))