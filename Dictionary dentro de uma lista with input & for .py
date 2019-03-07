
brasil = []
estado = {}

for _ in range(2):
    estado['Nome Estado'] = input()
    estado['sigla'] = input()
    brasil.append(estado.copy())

print(brasil)

for i in brasil:
    for key, value in i.items():
        print(key, value)

print()

for e in brasil:
    for v in e.values():
        print(v, end= ' ')
    print()



