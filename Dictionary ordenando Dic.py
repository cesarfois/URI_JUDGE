from time import sleep
from operator import itemgetter
jogo_ordenado = dict()
jogo = {'Jogador1': 6,
        'Jogador2': 2,
        'Jogador3': 8}

print(jogo)

jogo_ordenado = dict(sorted(jogo.items(), key=itemgetter(1), reverse=True))

#ordenar com multiples
#l = sorted(l, key=itemgetter(0, 1))

print(jogo_ordenado)

for k, v in jogo_ordenado.items():
    print(k,v)
sleep(2)
print(type(jogo_ordenado))


