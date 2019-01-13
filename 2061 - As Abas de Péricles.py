
abas, acoes = map(int,input().split())

for i in range(acoes):
    n = input()
    if n == 'fechou':
        abas += 1
    if n == 'clicou':
        abas -= 1

print(abas)