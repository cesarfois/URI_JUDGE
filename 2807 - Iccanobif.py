n = int(input())
t1 = 0
t2 = 1
res =[1]
i = 2
res2 = ''
while i <= n:
    t3 = t1 + t2
    res.append(t3)
    t1 = t2
    t2 = t3
    i += 1
res.sort(reverse=True)
for i in res:
    res2 += str(i) + ' '

print(res2[:-1])

