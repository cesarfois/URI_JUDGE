
A, G, D, a = 0, 0, 0, 0

while a != 4:
    a = int(input())

    if a == 1:
        A += 1

    elif a == 2:
        G += 1

    elif a == 3:
        D += 1

print("MUITO OBRIGADO")
print("Alcool: %d" %A)
print("Gasolina: %d" %G)
print("Diesel: %d" %D)