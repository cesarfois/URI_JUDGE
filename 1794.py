n = int(input())
a, b = map(int,input().split())
c, d = map(int,input().split())

if a <= n <= b and c <= n <= d:
    print('possivel')
else:
    print('impossivel')