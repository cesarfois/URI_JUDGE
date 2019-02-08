n = int(input())
for _ in range(n):
    k = int(input())
    l = list(map(int,input().split()))
    l1 = []
    l2 = []
    res = ''
    for i in l:
        if i % 2 != 0:
            l1.append(i)

    while len(l1) > 1:
        l2.append(max(l1))
        l1.remove(max(l1))
        l2.append(min(l1))
        l1.remove(min(l1))
    if len(l1) == 1:
        l2.append(min(l1))

    for w in l2:
        res += str(w) + ' '

    print(res[:-1])

