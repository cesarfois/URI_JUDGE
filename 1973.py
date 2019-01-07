print('='*72)
print('{0:=^72}'.format(' URI 1973 PYTHON'))
print('='*72)
print('{0:=^72}'.format(' Jornada nas Estrelas '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' fois2010@gmail.com '))
print('{0:=^72}'.format(' https://cesarfois.github.io/ '))
print('='*72)
print('')


n = int(input())

l = list(map(int,input().split()))
temp, res, i = 0, 0, 0

while i < n and (l[i] % 2 != 0):
    if l[i] >= 1:
        l[i] = l[i] - 1
    i += 1
    temp = i

if temp != n:
    temp = temp + 1
    for e in reversed(range(temp)):
            if l[e] >= 1:
               l[e] = l[e] - 1

for w in range(n):
    res = res + l[w]

print(temp, res)