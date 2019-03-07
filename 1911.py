# Problema esquisito ...
l = []
l1 = []
l2 = []
res = 0
n = int(input())
for i in range(n):
    a, b = input().split()
    l.append(a)
    l.append(b)
n1 = int(input())
for i in range(n1):
    c, d = input().split()
    l1.append(c)
    l1.append(d)

print(l)
print(l1)

for i in range(len(l)):
    if i % 2 == 0:
       a = l1.find(l[i])





for i in range(len(l)):
    if len(set(l[i]) - set(l1[i])) > 1:
        res += 1

print(res)


