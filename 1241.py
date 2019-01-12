
n = int(input())
for i in range(n):

    s, s1 = map(str,input().split())

    a = len(s1)
    res = s[-a:]
    if res == s1:
        print('encaixa')
    else:
        print('nao encaixa')