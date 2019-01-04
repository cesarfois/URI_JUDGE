var = float(input())

if (var >= 0) and (var <= 25):
    print('Intervalo [0,25]')
elif (var > 25) and (var <= 50):
    print('Intervalo (25,50]')
elif (var > 50) and (var <= 75):
    print('Intervalo (50,75]')
elif (var > 75) and (var <= 100):
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')
