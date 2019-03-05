import math
a, b = map(int, input().split())
res = 0

dif = abs(a-b)
res = b/dif
print(math.ceil(res))

