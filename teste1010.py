
n = int(input())

matriz = [0]*n

for i in range(n):
    matriz[i] = [1] * n
res = 1
for e in range(1, n - 1):
    for r in range(1, n - 1):
        if e == r:
            res += 1
        print('matriz[%d][%d] = %d' %(e,r,res) )

print()
matriz[1][1] = 2
matriz[1][2] = 2
matriz[1][3] = 2
matriz[1][4] = 2

matriz[2][1] = 2
matriz[2][2] = 3
matriz[2][3] = 3
matriz[2][4] = 2

matriz[3][1] = 2
matriz[3][2] = 3
matriz[3][3] = 3
matriz[3][4] = 2

matriz[4][1] = 2
matriz[4][2] = 2
matriz[4][3] = 2
matriz[4][4] = 2


print(matriz)

for c in range(n):
    print(matriz[c])

