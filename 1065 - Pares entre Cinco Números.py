c = 0
soma = 0
for x in range(1, 6, 1):
    a = float(input())
    if a % 2 == 0:
        c = c + 1


print('%d valores pares' % c)