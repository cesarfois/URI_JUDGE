n = int(input())

l = list(map(int,input().split()))
c2,c3,c4,c5 = 0,0,0,0
for i in l:
    if i % 2 == 0:
        c2 += 1
    if i % 3 == 0:
        c3 += 1
    if i % 4 == 0:
        c4 += 1
    if i % 5 == 0:
        c5 += 1

print('%d Multiplo(s) de 2' % c2)
print('%d Multiplo(s) de 3' % c3)
print('%d Multiplo(s) de 4' % c4)
print('%d Multiplo(s) de 5' % c5)