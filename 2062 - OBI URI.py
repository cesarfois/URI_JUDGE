
n = int(input())
l = []
l = list(map(str,input().split()))
s = ''
for i in l:
    if len(i) == 3:
        if i[0:2] == 'UR':
            s += 'URI' + ' '
        elif i[0:2] == 'OB':
            s += 'OBI' + ' '
        else:
            s += i + ' '
    else:
        s += i + ' '
s = s.rstrip()
print(s)