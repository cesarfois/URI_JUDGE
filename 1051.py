x = float(input())
if (x > 0.00) and (x < 2000.00):
    print('Isento')


elif(x >= 2000.01) and (x <= 3000.00):
    resto = x - 2000
    res = resto * 0.08
    print("R$ %.2f" % res)

elif (x >= 3000.01) and (x <= 4500.00):
    resto = x - 3000
    res = (resto * 0.18) + (1000 * 0.08)
    print("R$ %.2f" % res)

else:
    resto = x - 4500
    res = (resto * 0.28) + (1500 * 0.18) + (1000 * 0.08)
    print("R$ %.2f" % res)