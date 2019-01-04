p, j1, j2, r, a = map(int, input().split())

t = j1 + j2

if r == 0 and a == 0:
    if p == 1 and (t % 2 == 0):
        res = 'win1'
    elif p == 0 and (t % 2 != 0):
        res = 'win1'
    else:
        res = 'win2'
else:
    if r == 1 and a == 0:
        res = 'win1'
    elif r == 0 and a == 1:
        res = 'win1'
    elif r == 1 and a == 1:
        res = 'win2'

if res == 'win1':
    print('Jogador 1 ganha!')
if res == 'win2':
    print('Jogador 2 ganha!')