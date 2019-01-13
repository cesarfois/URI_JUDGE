res, d = 0, 2

for i in range(3, 40, 2):
    res = res + (float(i)/float(d))
    d = d * 2
res = res + 1

print('%.2f' % res)