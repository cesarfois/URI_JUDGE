import math
a, b = map(int, input().split())

q = a / b

if b > 0:
    q = float (a / b)
    q = int(math.floor(q))
else:
    q = float (a / b)
    q = int(math.ceil(q))

r = a - q * b


print("%d %d" % (q, r))

