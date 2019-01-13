

lista = input().split()

a = int(lista[0])
b = int(lista[1])

if a == 1:
    c = b * 4.00
elif a == 2:
    c = b * 4.50
elif a == 3:
    c = b * 5.00
elif a == 4:
    c = b * 2.00
elif a == 5:
    c = b * 1.50

print("Total: R$ %.2f" % c)