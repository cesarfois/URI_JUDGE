l = []
n = int(input())
for i in range(n):
    a = input()
    l.append(a)

l.sort()
l.sort(key=str.lower)

for x in l:
    print(x)