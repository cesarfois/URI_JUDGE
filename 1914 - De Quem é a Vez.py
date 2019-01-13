n = int(input())
lista = []
for i in range(n):
    lista = list(map(str,input().split()))
    v1, v2 = map(int,input().split())
    if lista[1] == 'PAR':
        if (v1 + v2) % 2 == 0:
            print(lista[0])
        else:
            print(lista[2])
    else:
        if (v1 + v2) % 2 == 0:
            print(lista[2])
        else:
            print(lista[0])

