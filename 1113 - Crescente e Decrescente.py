

while True:
    val = input().split()
    n = int(val[0])
    m = int(val[1])
    if (n == m):
        break
    if n < m:
        print('Crescente')
    else:
        print('Decrescente')