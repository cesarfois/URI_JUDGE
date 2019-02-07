while True:
    lista = []
    try:
        a = input()
        if a not in lista:
            lista.append(a)
    except EOFError:
        print(len(lista))
        break