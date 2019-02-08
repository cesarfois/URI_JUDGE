
e, d = map(int,input().split())

if e <= d:
    if e <= d and (d-e) >= 3:
        print('Muito bem! Apresenta antes do Natal!')
    elif e <= d and (d-e) <= 3:
        print('Parece o trabalho do meu filho!')
        if e+2 < 24:
            print('TCC Apresentado!')
        else:
            print('Fail! Entao eh nataaaaal!')
else:
    print('Eu odeio a professora!')