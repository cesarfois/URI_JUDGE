valor = int(input())
anos = float(valor) / 365
resto = float(valor) % 365
mes = resto / 30
resto = resto % 30
dias = resto / 1

print("%d ano(s)\n%d mes(es)\n%d dia(s)" % (anos, mes, dias))