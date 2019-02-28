pa, pg, ka, kg = map(float, input().split())


ta = pa / ka
tg = pg / kg

if ta == tg:
    print('G')
elif ta < tg:
    print('A')
else:
    print('G')