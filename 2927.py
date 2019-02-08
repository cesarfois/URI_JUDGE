al, comp, quei, sofx = map(int,input().split())


computdisponiveis = comp - quei - 1 - sofx


if computdisponiveis >= al:
    print('Igor feliz!')
elif computdisponiveis < al:
    if quei > sofx/2:
        print('Caio, a culpa eh sua!')
    else:
        print('Igor bolado!')