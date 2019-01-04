
linha1 = input().split()

a = int(linha1[0])
b = int(linha1[1])
c = int(linha1[2])

r = ((a + b) + abs(a - b)) / 2
res = ((r + c) + abs(r - c)) / 2

print("%d eh o maior" %res)

