n = int(input())
lp = []
li = []
for i in range(n):
    x = int(input())

    if x % 2 == 0:
        lp.append(x)
    else:
        li.append(x)

lp.sort()
li.sort(reverse=True)

for i in lp:
    print(i)
for e in li:
    print(e)