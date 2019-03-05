n = int(input())

for i in range(n):
    c, v = map(int,input().split())
    res = int(c / v) + int(c % v)
    print(res)