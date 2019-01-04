

lista = input().split()

n1 = float(lista[0])
n2 = float(lista[1])
n3 = float(lista[2])
n4 = float(lista[3])

m = ((n1 * 2.0) + (n2 * 3.0) + (n3 * 4.0) + (n4 * 1.0)) / (2.0 + 3.0 + 4.0 + 1.0)

print("Media: %.1f" % m)

if m >= 7.0:
    print("Aluno aprovado.")
elif m < 5.0:
    print("Aluno reprovado.")
elif (m >= 5.0) and (m <= 6.9):
    print("Aluno em exame.")
    ne = float(input())
    print("Nota do exame: %.1f" % ne)
    nfinal = (m + ne)/2
    if nfinal >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % nfinal)