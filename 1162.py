n = int(input())
for i in range(n):
    fim = int(input())
    l = list(map(int, input().split()))
    c = 0
    while fim > 1:
        trocou = False
        x = 0
        while x < (fim - 1):
            if l[x] > l[x+1]:
                trocou = True
                c += 1
                temp = l[x]
                l[x] = l[x + 1]
                l[x + 1] = temp
            x += 1
        if not trocou:
            break
        fim -= 1
    print('Optimal train swapping takes %d swaps.' % c)
