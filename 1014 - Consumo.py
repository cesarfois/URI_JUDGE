'''
um valor inteiro X representando a distância total percorrida (em Km),
m valor real Y representando o total de combustível gasto, com um dígito após o ponto decimal.

'''

x = int(input())
y = float(input())

print("%.3f km/l" % (x / y))
