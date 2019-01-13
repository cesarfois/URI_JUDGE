n = input()

res = 0

for i in n:
    if int(i) == 1:
        res += 1
if res % 2 == 0:
    print(n, end='' + '0\n')
else:
    print(n, end='' + '1\n')