n = int(input())
res2 = ''

if n == 0:
    print('0')
    n = -1
else:
    t1 = 0
    t2 = 1
    res2 = '0 1 '
i = 2
while i < n:
    t3 = t1 + t2
    res2 += str(t3) + ' '
    t1 = t2
    t2 = t3
    i += 1
print(res2[:-1])