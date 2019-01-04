valor = int(input())
horas = float(valor) / 3600
resto = float(valor) % 3600

min = resto / 60
resto = resto % 60

seg = resto / 1
resto = resto % 1

print("%d:%d:%d" % (horas, min, seg))