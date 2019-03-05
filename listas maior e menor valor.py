l = [4, 9, 34, 90]

maior = 0
menor = 0

for i in range(len(l)):
    if i == 0:
        maior = menor = l[i]
    else:
        if l[i] > maior:
            maior = l[i]
        if l[i] < menor:
            menor = l[i]

print(menor)
print(maior)