c = 0
soma = 0
for x in range(1,7,1):
    a = float(input())
    if a > 0:
        c = c + 1
        soma = soma + a

print('%d valores positivos' % c)
print('%.1f' % (soma/c))