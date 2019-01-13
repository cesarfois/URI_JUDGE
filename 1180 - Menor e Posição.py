n = int(input())

lista = list(map(int, input().split()))

temp = lista[0]
pos, count = 0, 0

for i in lista:
    if i < temp:
        temp = i
        pos = count
    count += 1

print('Menor valor: %d' % temp)
print('Posicao: %d' % pos)