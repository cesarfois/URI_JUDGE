
string = input().split()

a = float(string[0])
b = float(string[1])
c = float(string[2])
lista = [a, b, c]
lista.sort(reverse=True)
a = lista[0]
b = lista[1]
c = lista[2]

if a >= (b + c):
    print('NAO FORMA TRIANGULO')
if (a ** 2) == (b ** 2) + (c ** 2):
    print('TRIANGULO RETANGULO')
if ((a ** 2) > (b ** 2) + (c ** 2)) and ((a + b) > c ) and ((b + c) > a) and ((a + c) > b):
    print('TRIANGULO OBTUSANGULO')
if (a ** 2) < (b ** 2) + (c ** 2):
    print('TRIANGULO ACUTANGULO')
if a == b == c:
    print('TRIANGULO EQUILATERO')
if ((a == b) and (b != c)) or ((b == c) and (a != b)) or ((a == c) and (c != b)):
    print('TRIANGULO ISOSCELES')
