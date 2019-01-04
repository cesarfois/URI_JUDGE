empate, tinter, tgremio = 0, 0, 0
continuar = "S"
while continuar == "S":
    a = 4
    val = input().split()
    inter = int(val[0])
    gremio = int(val[1])
    if inter == gremio:
        empate = empate + 1
    elif inter > gremio:
        tinter = tinter + 1
    else:
        tgremio = tgremio + 1

    while a != 1 and a != 2:
        print('Novo grenal (1-sim 2-nao)')
        a = int(input())

        if a == 1:
            continuar = "S"
        elif a == 2:
            continuar = 'N'
        else:
            print('Novo grenal (1-sim 2-nao)')
            a = int(input())

print('%d grenais' %(tgremio + tinter + empate))
print('Inter:%d' % tinter)
print('Gremio:%d' % tgremio)
print('Empates:%d' % empate)
if tinter > tgremio:
    print('Inter venceu mais')
elif tgremio > tinter:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
