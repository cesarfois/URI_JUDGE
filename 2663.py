totcomp = int(input())
notas = []
l = []
clasif = int(input())
for _ in range(totcomp):
    notas.append(int(input()))
notas.sort(reverse=True)

qdeclase = 0
cont = 0
ultimo = 0
for x in notas:

    if clasif > 0:
        qdeclase += 1
        ultimo = x
    elif x == ultimo:
        qdeclase += 1

    cont += 1
    clasif -= 1

print(qdeclase)