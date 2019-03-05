n = int(input())
l = []
sinal = []
for i in range(n):
    a, b = map(str, input().split())
    l.append(b)
    sinal.append(a)
l.sort()
for e in l:
    print(e)

print('Se comportaram: %d | Nao se comportaram: %d' %(sinal.count('+'),sinal.count('-')))