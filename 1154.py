idade ,c, soma = 0, 0, 0

while True:
    idade = int(input())
    if idade >= 0:
        soma = soma + idade
        c += 1
    else:
       break

print('%.2f' %(soma/c))
