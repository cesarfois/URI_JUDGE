# nao foi finalizado
n = int(input())
l = []
l = list(map(str,input().split()))
s = ''
print(l)
for i in l:
    if len(i) >= 11 and len(i) <= 12:
        if i[1:9] == 'oulupukk':
            s += 'Joulupukki' + ' '
        else:
            s += i + ' '
    else:
        s += i + ' '
    s = s.rstrip()
    print(s)