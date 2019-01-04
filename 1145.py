val = input().split()
lim = int(val[0])
y = int(val[1])

c = 1

for i in range(1, y + 1):
    if c == lim:
        print(i)
        c = 1
    else:
        print(i, end=' ')
        c += 1