from operator import itemgetter

lres = [{'ord': 66, 'contador': 2}, {'ord': 67, 'contador': 1}, {'ord': 65, 'contador': 3}]
#nova lista = sorted(lista a ordenar, key = itemgetter(nome do value)
lres = sorted(lres, key=itemgetter('contador'))