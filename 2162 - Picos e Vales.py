n = int(input())

l = list(map(int,input().split()))

res = 1
if n == 2 and l[0] == l[1]:
    res = 0
for i in range(2,n):
    if l[i] >= l[i-1] and l[i-1] >= l[i-2]:
        res = 0
    elif l[i] <= l[i-1] and l[i-1] <= l[i-2]:
        res = 0


if res == 0:
    print('0')
else:
    print('1')