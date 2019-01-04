valor = float(input())

print("NOTAS:")


n100 = valor / 100
resto = valor % 100
print("%d nota(s) de R$ 100.00" %n100)
n50 = resto / 50
resto = resto % 50
print("%d nota(s) de R$ 50.00" %n50)
n20 = float(resto / 20)
resto = float(resto % 20)
print("%d nota(s) de R$ 20.00" %n20)
n10 = float(resto / 10)
resto = float(resto % 10)
print("%d nota(s) de R$ 10.00" %n10)
n5 = float(resto / 5)
resto = float(resto % 5)
print("%d nota(s) de R$ 5.00" %n5)
n2 = float(resto / 2)
resto = float(resto % 2)
print("%d nota(s) de R$ 2.00" %n2)
print("MOEDAS:")


m1 = float(resto / 1)
resto = float(resto % 1)


print("%d moeda(s) de R$ 1.00" %m1)
m50 = float(resto / 0.50)
resto = float(resto % 0.50)
print("%d moeda(s) de R$ 0.50" %m50)
m25 = float(resto / 0.25)
resto = float(resto % 0.25)
print("%d moeda(s) de R$ 0.25" %m25)
m10 = float(resto / 0.10)
resto = float(resto % 0.10)
print("%d moeda(s) de R$ 0.10" %m10)
m5 = float(resto / 0.05)
resto = float(resto % 0.05)
print("%d moeda(s) de R$ 0.05" %m5)
m1 = float(resto / 0.01)
resto = float(resto % 0.01)
print("%d moeda(s) de R$ 0.01" %m1)