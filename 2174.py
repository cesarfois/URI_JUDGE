n = int(input())
l = []
for i in range(n):
    s = input()
    if s not in l:
        l.append(s)

res = 151 - len(l)
print('Falta(m) %d pomekon(s).' % res)