
n = int(input())

matriz = [0]*n
for e in range(n):
    for i in range(n):
        matriz[i] = [1] * n

for c in range(n):
    print(matriz[c])


