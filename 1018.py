valor = float(input())

print("%.0f" %valor)


n100 = valor / 100
resto = valor % 100

print("%d nota(s) de R$ 100,00" %n100)
n50 = resto / 50
resto = resto % 50
print("%d nota(s) de R$ 50,00" %n50)
n20 = float(resto / 20)
resto = int(resto % 20)
print("%d nota(s) de R$ 20,00" %n20)
n10 = float(resto / 10)
resto = int(resto % 10)
print("%d nota(s) de R$ 10,00" %n10)
n5 = float(resto / 5)
resto = int(resto % 5)
print("%d nota(s) de R$ 5,00" %n5)
n2 = float(resto / 2)
resto = int(resto % 2)
print("%d nota(s) de R$ 2,00" %n2)
n1 = float(resto / 1)
resto = int(resto % 1)
print("%d nota(s) de R$ 1,00" %n1)