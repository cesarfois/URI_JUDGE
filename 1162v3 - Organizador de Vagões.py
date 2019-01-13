
fim = int(input())
l = list(map(int, input().split()))
c = 0
ln = []
for anterior in range(4):
    for chave, valor in enumerate(l):
        if l[anterior] <= valor:
            ln.insert(chave, l[anterior])
            c+=1
            break
        else:
            ln.append(l[anterior])




print(ln)
print(c)


print('Optimal train swapping takes %d swaps.' % c)
