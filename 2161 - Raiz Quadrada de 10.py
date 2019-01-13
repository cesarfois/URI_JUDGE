n = int(input())
x = 0
for i in range(n):
    x += 6.0
    x = (1.0 / x)

x = x + 3.00
print('%.10f' % x)