lista = []
for i in range(20):
    n = int(input())
    lista.append(n)

pos = 0
for l in lista[::-1]:
    print("N[%d] = %d" %(pos,l))
    pos += 1