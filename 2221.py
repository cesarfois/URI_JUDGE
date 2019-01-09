n = int(input())

for i in range(n):
    res, res1 = 0, 0
    b = int(input())
    a, d, l = map(int,input().split())
    a1, d1, l1 = map(int, input().split())

    res = (a + d) / 2

    if l % 2 == 0:
        res = res + b

    res1 = (a1 + d1) / 2
    if l1 % 2 == 0:
        res1 = res1 + b


    if res > res1:
        print('Dabriel')
    if res < res1:
        print('Guarte')
    if res == res1:
        print('Empate')