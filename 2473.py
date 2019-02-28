l = list(map(int, input().split()))
r = list(map(int, input().split()))

res = 0

for i in l:
    if i in r:
        res += 1

if res == 6:
    print('sena')
elif res == 5:
    print('quina')
elif res == 4:
    print('quadra')
elif res == 3:
    print('terno')
elif res < 3:
    print('azar')


