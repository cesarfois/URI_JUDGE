matriz = [[2, 2, 2 ],[4, 4, 4],[6, 6, 6]]
somapar = 0
som3racol = 0
soma2dalinha = 0
for l in range(0, 3):
    for c in range(0, 3):
        print(matriz[l][c], end= ' ')
        # somar todos numeros pares da matriz
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()

# somar os numeros da terceira coluna.

for l in range(0, 3):
    som3racol += matriz[l][2]

for c in range(0, 3):
    soma2dalinha += matriz[1][c]


print(somapar , som3racol, soma2dalinha)