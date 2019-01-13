
string = input().split()

a = float(string[0])
b = float(string[1])
c = float(string[2])

if ((a + b) > c ) and ((b + c) > a) and ((a + c) > b):
    print('Perimetro = %.1f' % (a + b + c))
else:
    print('Area = %.1f' % (((a + b) * c)/2))
