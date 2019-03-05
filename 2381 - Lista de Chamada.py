a,k = map(int,input().split())
l=['']
for i in range(a):
    l.append(input())
l.sort()
print(l[k])