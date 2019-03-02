
l =[8, 10, 7, 4, 5, 6, 3, 1, 9, 2]

# explorando os elementos.
for i in l:
    print(i, end=' ')
print()

# explorando as posiçoes e elementos.
for e in range(len(l)):
    print(l[e], end= ' ')
print()
# utilizando o enumerate.
for venum , elementol in enumerate(l):
    print(venum, elementol, end=' ')