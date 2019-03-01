n = int(input())
res = 0
for i in range(n):
    l, c = map(int,input().split())
    if l > c:
        res += c
print(res)