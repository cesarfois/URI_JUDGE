l = list(map(int,input().split()))
lista = ['Rudolph', 'Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen' ]
a = sum(l) % 9

print(lista[a])