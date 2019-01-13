qde, soma = 0, 0

while qde < 2:
    nota = float(input())

    if nota > 0.0 and nota <= 10.0:
        soma = soma + nota
        qde = qde + 1
    else:
        print('nota invalida')

print('media = %.2f' % (soma/2))