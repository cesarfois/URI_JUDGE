n = int(input())
ssoma, bsoma, asoma= 0,0,0
s1soma, b1soma, a1soma= 0,0,0

for i in range(n):
    nome = input()
    s,b,a = map(int,input().split())
    s1, b1, a1 = map(int, input().split())
    ssoma += s ; bsoma += b ; asoma += a
    s1soma += s1 ; b1soma += b1 ; a1soma += a1

st = (s1soma * 100) / ssoma
bt = (b1soma * 100) / bsoma
at = (a1soma * 100) / asoma

print('Pontos de Saque: %.2f ' % st + "%.")
print('Pontos de Bloqueio: %.2f ' % bt + "%.")
print('Pontos de Ataque: %.2f ' % at + "%.")


