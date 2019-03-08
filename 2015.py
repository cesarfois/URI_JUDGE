n = int(input())
res = 0

lista = [['F', 'A', 'C', 'E']]
for i in range(n):
    l = []
    l = list(map(str,input().split()))
    lista.append(l)

print(lista)
