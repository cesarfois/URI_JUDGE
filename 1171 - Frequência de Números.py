n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
l1 = sorted(set(l))

for i in l1:
    res = l.count(i)
    print('%d aparece %d vez(es)' % (i, res))
