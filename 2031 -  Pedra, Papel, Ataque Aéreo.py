n = int(input())

for i in range(n):
    a = input()
    b = input()

    if a == 'ataque' and b == 'pedra':
        print('Jogador 1 venceu')
    elif a == 'pedra' and b == 'ataque':
        print('Jogador 2 venceu')

    elif a == 'pedra' and b == 'papel':
        print('Jogador 1 venceu')
    elif a == 'papel' and b == 'pedra':
        print('Jogador 2 venceu')

    elif a == 'ataque' and b == 'papel':
        print('Jogador 1 venceu')
    elif a == 'papel' and b == 'ataque':
        print('Jogador 2 venceu')

    elif a == 'papel' and b == 'papel':
        print('Ambos venceram')

    elif a == 'pedra' and b == 'pedra':
        print('Sem ganhador')

    elif a == 'ataque' and b == 'ataque':
        print('Aniquilacao mutua')

