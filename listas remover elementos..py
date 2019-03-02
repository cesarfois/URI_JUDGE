l = [4,2,'*',2,3,'ultimo']

# deletar elementos na posicao desejada.
del l[2]

# deletar elem, normalmente utilizado para o ultimo, mas pode ser usado para escolher um pos
l.pop(4)

# deletar pelo nome do elemento.
l.remove(2)
# cuidado que se nao existe o elemento da erro entao usar assim
for i in l:
    if i == 2:
        l.remove(2)

print(l)
