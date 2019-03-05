v, a = map(int, input().split())

l = list(map(int,input().split()))

for i in l:
    v += i
    if v > 100:
        v = 100
    if v < 0:
        v = 0

print(v)