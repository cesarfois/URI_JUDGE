a,b,c = map(int,input().split())
l = [a,b,c]
l = sorted(l)
a, b, c = l[2], l[1], l[0]

if a + b > c and b + c > a and a + c > b:

    if a*a == b*b + c*c:
        rect = 'S'
    else:
        rect = 'N'
    if a == b and b == c and a == c :
        print('Valido-Equilatero')
        print('Retangulo: %s' % rect)
    elif a != b and b != c and a != c:
        print('Valido-Escaleno')
        print('Retangulo: %s' % rect)
    elif a == b or b == c or a == c:
        print('Valido-Isoceles')
        print('Retangulo: %s' % rect)
else:
    print('Invalido')
