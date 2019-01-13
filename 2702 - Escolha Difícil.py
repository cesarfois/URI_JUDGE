
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

res = 0
for i in range(3):
    if l2[i] >= l1[i]:
        res = res + (l2[i] - l1[i])

print(res)




