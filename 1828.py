n = int(input())

for i in range(n):
    a, b = map(str, input().split())

    if a == 'papel' and b == 'pedra':
        print('Caso #%d: Bazinga!' % (i + 1))
    elif a == 'pedra' and b == 'papel':
        print('Caso #%d: Raj trapaceou!' % (i + 1))
    elif a == 'tesoura' and b == 'papel':
        print('Caso #%d: Bazinga!' % (i + 1))
    elif a == 'papel' and b == 'tesoura':
        print('Caso #%d: Raj trapaceou!' % (i + 1))

    elif a == 'pedra' and b == 'lagarto':
        print('Caso #%d: Bazinga!' % (i + 1))
    elif a == 'lagarto' and b == 'pedra':
        print('Caso #%d: Raj trapaceou!' % (i + 1))


    elif a == 'lagarto' and b == 'Spock':
        print('Caso #%d: Bazinga!' % (i + 1))
    elif a == 'Spock' and b == 'lagarto':
        print('Caso #%d: Raj trapaceou!' % (i + 1))

    elif a == 'Spock' and b == 'tesoura':
        print('Caso #%d: Bazinga!' % (i + 1))
    elif a == 'tesoura' and b == 'Spock':
        print('Caso #%d: Raj trapaceou!' % (i + 1))

    elif a == 'tesoura' and b == 'lagarto':
        print('Caso #%d: Bazinga!' % (i + 1))
    elif a == 'lagarto' and b == 'tesoura':
        print('Caso #%d: Raj trapaceou!' % (i + 1))

    elif a == 'lagarto' and b == 'papel':
        print('Caso #%d: Bazinga!' % (i + 1))
    elif a == 'papel' and b == 'lagarto':
        print('Caso #%d: Raj trapaceou!' % (i + 1))

    elif a == 'papel' and b == 'Spock':
        print('Caso #%d: Bazinga!' % (i + 1))
    elif a == 'Spock' and b == 'papel':
        print('Caso #%d: Raj trapaceou!' % (i + 1))

    elif a == 'Spock' and b == 'pedra':
        print('Caso #%d: Bazinga!' % (i + 1))
    elif a == 'pedra' and b == 'Spock':
        print('Caso #%d: Raj trapaceou!' % (i + 1))

    elif a == 'pedra' and b == 'tesoura':
        print('Caso #%d: Bazinga!' % (i + 1))
    elif a == 'tesoura' and b == 'pedra':
        print('Caso #%d: Raj trapaceou!' % (i + 1))
    else:
        print('Caso #%d: De novo!' % (i + 1))

