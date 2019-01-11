def troca(l, fim, c):
    for j in range(fim):
        for k in range((j + 1), fim):
            if l[j] > l[k]:
                aux = l[j]
                l[j] = l[k]
                l[k] = aux
    c = 3
    return c

n = int(input())
for e in range(n):
        fim = int(input())
        l = list(map(int, input().split()))
        c = 5
        troca(l, fim)
        print(l, c)
        print('Optimal train swapping takes %d swaps.' % c)
