'''

10.0 20.1 5.1

(b**2) - (4ac)

'''

linha = input().split()


a = float(linha[0])
b = float(linha[1])
c = float(linha[2])

d = (b**2) - (4 * a * c)

if (d >= 0) and (a != 0):
    r1 = (-b + (d ** (1/2))) / (2 * a)
    r2 = (-b - (d ** (1/2))) / (2 * a)
    print("R1 = %.5f\nR2 = %.5f" % (r1, r2))
else:
    print('Impossivel calcular')

