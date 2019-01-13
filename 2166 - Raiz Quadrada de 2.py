
n = int(input())
x = 0
for i in range(n):
    x += 2.0
    x = (1.0 / x)

x = x + 1.00
print('%.10f' % x)