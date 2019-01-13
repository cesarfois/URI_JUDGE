lista = list(map(int,input().split()))
soma = 0
listv = []

for i in lista:
    if i > 0:
        listv.append(i)

a = int(listv[0])
n = int(listv[1])

for i in range(n):
    soma += a
    a += 1

print("%d" % soma)
