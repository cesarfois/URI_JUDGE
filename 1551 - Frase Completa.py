
n = int(input())
for _ in range(n):
    s = input()
    s1 = 'abcdefghijklmnopqrstuvwxyz'
    c = 0
    for i in s1:
        if i in s:
            c += 1
    if c < 13:
        print('frase mal elaborada')
    elif c < 26:
        print('frase quase completa')
    elif c >= 26:
        print('frase completa')
