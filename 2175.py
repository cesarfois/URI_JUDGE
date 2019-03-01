o, b, i = map(float, input().split())

if o < b and o < i:
    print('Otavio')
elif b < o and b < i:
    print('Bruno')
elif i < o and i < b:
    print('Ian')
else:
    print('Empate')


