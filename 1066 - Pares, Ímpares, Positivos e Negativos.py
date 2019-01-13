soma, pos, neg, c, i = 0,0,0,0,0

for x in range(1, 6, 1):
    a = float(input())
    if a % 2 == 0:
        c = c + 1
    else:
        i = i + 1
    if a > 0:
        pos = pos + 1
    if a < 0:
        neg = neg + 1

print('%d valor(es) par(es)' % c)
print('%d valor(es) impar(es)' % i)
print('%d valor(es) positivo(s)' % pos)
print('%d valor(es) negativo(s)' % neg)
