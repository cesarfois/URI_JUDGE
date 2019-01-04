linha1 = input().split()

A, B, C = linha1

tri = (float(A) * float(C)) / 2
cir = (3.14159 * (float(C) ** 2))
trap = ((float(A) + float(B)) * float(C)) / 2
quad = float(B) * float(B)
rect = float(A) * float(B)

print("TRIANGULO: %.3f" % tri)
print("CIRCULO: %.3f" % cir)
print("TRAPEZIO: %.3f" % trap)
print("QUADRADO: %.3f" % quad)
print("RETANGULO: %.3f" % rect)

'''

TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
QUADRADO: 16.000
RETANGULO: 12.000

'''
