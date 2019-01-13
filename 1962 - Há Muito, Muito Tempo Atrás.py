n = int(input())

for i in range(n):
    ent = int(input())
    if ent < 2015:
        res = 2015 - ent
        print('%d D.C.' % res)
    elif ent >= 2015:
        res = ent - 2014
        print('%d A.C.' % res)