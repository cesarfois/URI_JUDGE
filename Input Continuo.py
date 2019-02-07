while True:
    try:
        l = []
        while True:
            a = input()
            if len(a) == 0:
                break
            l.append(a)
        print(l)
    except EOFError:
        break

a = ')'
lista = []
while a[:1] == ')' or a[:1] == '(':
    try:
        a = str(input())
        if a not in lista and (a[:1] == ')' or a[:1] == '('):
            lista.append(a)
    except EOFError:
        break
print(len(lista))