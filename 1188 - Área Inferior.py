operacao = input()
soma = 0
lin = 12
qde = 0

for c in range(12):
    lin = lin - 1
    for j in range(12):
        valor = float(input())
        if (j > lin) and (j < c):
            soma = soma + valor
            qde = qde + 1

if operacao == 'S':
    print("%.1f" % soma)
else:
    print("%.1f" % (soma/qde))