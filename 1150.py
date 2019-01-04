x = int(input())
z = 0
while True:
    z = int(input())
    if z > x:
        break

soma = x
c = 1

while z > soma:
    soma = soma + x
    c += 1
    x += 1

print(c)
