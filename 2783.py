tfig = list(map(int,input().split()))

figcar = list(map(int,input().split()))

compr = list(map(int,input().split()))

c = 0
for i in figcar:
    if i not in compr:
        c += 1

print(c)