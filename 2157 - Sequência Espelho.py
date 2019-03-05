n = int(input())

for w in range(n):

    a, b = map(int, input().split())
    res = ''
    for i in range(a,b+1):
        res += str(i)

    res += res[::-1]
    print(res)