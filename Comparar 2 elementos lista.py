l = list(map(int,input().split()))

pico = ''
res = 0
temp = ''
it4 = l[0]
it2 = l[0]
for i in range(len(l) - 1):
    print('l[i]=%d      l[i + 1]=%d      it2=%d     it4=%d '%(l[i], l[i + 1], it2, it4))

    if l[i] < l[i+1] and (pico == 'N' or pico == '') and it2 < l[i+1] :
        pico = 'P'
        it2 = l[i + 1]
        res += 1
        print(pico)

    if l[i] > l[i+1] and (pico == 'P' or pico == '')and it4 > l[i+1]:
        pico = 'N'
        it4 = l[i + 1]
        res += 1
        print(pico)


if l[0] < l[-1] and pico == 'P':
    res += 1
if l[0] > l[-1] and pico == 'N':
    res += 1


print(res)


