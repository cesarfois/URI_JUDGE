import math

while True:
    try:
        n = int(input())
        res = math.log2(n)
        print('%d' % res)

    except EOFError:
        break