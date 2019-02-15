dreg, prei, vprea, ndfut = map(int,input().split())

i=0
precototal = prei
while i < ndfut:
    dreg += 1
    if dreg % 2 == 0:
        precototal += vprea
    if dreg % 2 != 0:
        precototal -= vprea
    i += 1
print(precototal)