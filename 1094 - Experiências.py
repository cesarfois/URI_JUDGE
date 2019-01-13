n = int(input())
coelhos, ratos, sapos = 0, 0, 0
for x in range(n):
    val = input().split()
    if str(val[1]) == "C":
        coelhos = coelhos + (int(val[0]))
    if str(val[1]) == "R":
        ratos = ratos + (int(val[0]))
    if str(val[1]) == "S":
        sapos = sapos + (int(val[0]))


total = coelhos + ratos + sapos
print('Total: %d cobaias' % total)
print('Total de coelhos: %d' % coelhos)
print('Total de ratos: %d' % ratos)
print('Total de sapos: %d' % sapos)
print('Percentual de coelhos: %.2f' % ((coelhos * 100)/total) + ' %')
print('Percentual de ratos: %.2f' % ((ratos * 100)/total) + ' %')
print('Percentual de sapos: %.2f' % ((sapos * 100)/total) + ' %')