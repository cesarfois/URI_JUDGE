from fractions import Fraction

n = int(input())

for i in range(n):

    l = list(map(str,input().split()))

    a = int(l[0])
    b = int(l[2])
    op = l[3]
    c = int(l[4])
    d = int(l[6])

    if op == '+':
        a = (a*d + c*b)
        b = b * d

    elif op == '-':
        a = (a * d - c * b)
        b = b * d

    elif op == '*':
        a = (a * c)
        b = b * d

    elif op == '/':
        a = a * d
        b = c * b

    f = Fraction(int(a), int(b))

    print('%d/%d = %d/%d' % (a, b, f.numerator, f.denominator))
