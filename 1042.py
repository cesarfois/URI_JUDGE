
string = input().split()

a = int(string[0])
b = int(string[1])
c = int(string[2])

lista = [a, b, c]


lista.sort()

for i in range(3):
    print(lista[i])
print()

print(a)
print(b)
print(c)