n = int(input())

for i in range(n):
    a, b = map(str, input().split())

    if a == 'papel' and b == 'pedra':
        print('rajesh')
    elif a == 'pedra' and b == 'papel':
        print('sheldon')
    elif a == 'tesoura' and b == 'papel':
        print('rajesh')
    elif a == 'papel' and b == 'tesoura':
        print('sheldon')

    elif a == 'pedra' and b == 'lagarto':
        print('rajesh')
    elif a == 'lagarto' and b == 'pedra':
        print('sheldon')


    elif a == 'lagarto' and b == 'spock':
        print('rajesh')
    elif a == 'spock' and b == 'lagarto':
        print('sheldon')

    elif a == 'spock' and b == 'tesoura':
        print('rajesh')
    elif a == 'tesoura' and b == 'spock':
        print('sheldon')

    elif a == 'tesoura' and b == 'lagarto':
        print('rajesh')
    elif a == 'lagarto' and b == 'tesoura':
        print('sheldon')

    elif a == 'lagarto' and b == 'papel':
        print('rajesh')
    elif a == 'papel' and b == 'lagarto':
        print('sheldon')

    elif a == 'papel' and b == 'spock':
        print('rajesh')
    elif a == 'spock' and b == 'papel':
        print('sheldon')
    elif a == 'spock' and b == 'pedra':
        print('rajesh')
    elif a == 'pedra' and b == 'spock':
        print('sheldon')

    elif a == 'pedra' and b == 'tesoura':
        print('rajesh')
    elif a == 'tesoura' and b == 'pedra':
        print('sheldon')
    else:
        print('empate')

