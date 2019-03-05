n = int(input())
l = []
for w in range(n):
    l.append(input())

consegue = True
c = 0
pulos = 0
for i in l:
    if i[0] == '-':
        c = 0
    if i[0] == '.':
        if c == 0:
            pulos += 1
        c += 1
        if c >= 3:
            consegue = False
            break


if not consegue:
    print('N')
else:
    print(pulos)