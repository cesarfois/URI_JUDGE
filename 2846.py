n = int(input())
t1 = 0
t2 = 1
res =[1]
i = 2
l1 = [' ']
final = n + 100

while i <= final:
    t3 = t1 + t2
    res.append(t3)
    t1 = t2
    t2 = t3
    i += 1
c = 0

for i in range(1, final):
    if i not in res:
        l1.append(i)

print(l1)
print(res)
print(l1[n])