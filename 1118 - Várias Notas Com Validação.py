cont = "sim"
while cont == "sim":
    teste, qde, soma = 5, 0, 0

    while qde < 2:
        nota = float(input())
        if nota >= 0.0 and nota <= 10.0:
            soma = soma + nota
            qde = qde + 1
        else:
            print('nota invalida')
    print('media = %.2f' % (soma/2))

    while teste != 1 and teste != 2:
        teste = int(input('novo calculo (1-sim 2-nao)\n'))
        if teste == 1:
            cont = "sim"
        elif teste == 2:
            cont = 'nao'
        else:
            teste = int(input('novo calculo (1-sim 2-nao)\n'))


