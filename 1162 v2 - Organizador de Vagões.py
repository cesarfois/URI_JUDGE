for e in range(int(input())):
        fim = int(input())
        l = list(map(int, input().split()))
        c, aux = 0,0
        c = 0
        for j in range(fim):
            for k in range((j+1), fim):
                if l[j] > l[k]:
                    aux = l[j]
                    l[j] = l[k]
                    l[k] = aux
                    c+=1
        print('Optimal train swapping takes %d swaps.' % c)