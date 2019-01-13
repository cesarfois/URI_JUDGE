
n = int(input())
lista = list(map(int,input().split()))

resultado = 0
menor = lista[0]

for i in range(n):
    if lista[i] < menor:
        menor = lista[i]
        resultado = i

print(resultado + 1)