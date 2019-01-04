valor = float(input())
notas = [100, 50, 20, 10, 5, 2, 1]

print("%.0f" % valor)
for x in notas:
    n100 = valor / x
    valor = valor % x
    print("%d nota(s) de R$ %.2f" % (n100, x))