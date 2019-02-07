l = []
res = []
for _ in range(3):
    a = int(input())
    l.append(a)

res.append(l[1] * 2 + l[2] * 4)
res.append(l[0] * 2 + l[2] * 2)
res.append(l[0] * 4 + l[1] * 2)

print(min(res))