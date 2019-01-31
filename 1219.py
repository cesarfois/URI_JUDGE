while True:
    try:

        a,b,c = map(float,input().split())

        pi = 3.1415926535897
        #area do circulo Maior
        r = (a*b*c)/((a+b+c)*(b+c-a)*(c+a-b)*(a+b-c)) ** (1/2)
        ac = pi * (r * r)
        #Semi= perimetro
        p = (a + b + c)/2
        # Area do triangulo rectangulo, produtos dos catetos dividido 2
        at = (p * (((p-a) * (p-b)) * (p-c))) ** (1/2)
        # Area do circulo circunscrito a = semiperimetro * r => r = a /sem
        rcm = at/p
        # Area do circulo menor
        acm = pi * (rcm * rcm)

        print('%.4f %.4f %.4f' % ((ac - at),(at - acm), acm))

    except EOFError:
        break