for i in range(int(input())):
    l = list(map(int, input().split()))
    m = l[0]
    sum ,c = 0, 0
    for i in range(1, len(l)):
        sum += l[i]
    for e in range(1, len(l)):
        if l[e] > (sum/m):
            c += 1
    print('%.3f' % (c * 100 / m) + '%')




