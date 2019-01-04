
x = float(input())

if (x > 0.00) and (x <= 400.00):
    por = 15
if(x > 400.00) and (x <= 800.00):
    por = 12
if (x > 800.00) and (x <= 1200.00):
    por = 10
if (x > 1200.00) and (x <= 2000.00):
    por = 7
if x > 2000.00:
    por = 4

re = (x * por)/100

print("Novo salario: %.2f" % (x+re))
print("Reajuste ganho: %.2f" % re)
print('Em percentual: %d' % por + " %")