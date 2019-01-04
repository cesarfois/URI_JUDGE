b = 0
for x in range(100):
    a = int(input())
    if a > b:
        res = a
        pos = x
        b = a
print("%d" % res)
print('%d' % (pos + 1))
