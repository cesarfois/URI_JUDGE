while True:
    try:
        nat = int(input())

        ncm, ncl = map(int,input().split())
        lm = []
        lm1 = []
        ll = []
        ll1 = []

        for f in range(ncm):
            lm = list(map(int,input().split()))
            lm1.append(lm)

        for f in range(ncl):
            ll = list(map(int,input().split()))
            ll1.append(ll)

        cem, cel = map(int,input().split())
        atribc = int(input())

        if (lm1[cem - 1][atribc - 1]) > (ll1[cel - 1][atribc - 1]):
            print('Marcos')
        elif (lm1[cem - 1][atribc - 1]) < (ll1[cel - 1][atribc - 1]):
            print('Leonardo')
        elif (lm1[cem - 1][atribc - 1]) == (ll1[cel - 1][atribc - 1]):
            print('Empate')

    except EOFError:
        break
