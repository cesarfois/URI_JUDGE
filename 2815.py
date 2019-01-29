
l = []
l = list(map(str,input().split()))
res = ''

for i in l:
    if len(i) >= 4 and i[:2] == i[2:4]:
        res += i[2:] + ' '
    else:
        res += i + ' '

print(res[:-1])