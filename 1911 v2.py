
while True:
    try:
        orig = {}
        sala = {}
        cont = 0
        res = 0
        n = int(input())
        if n == 0:
            break
        for i in range(n):
            a, b = map(str,input().split())
            if len(a) > 20:
                break
            orig[a] = b
        n = int(input())
        for i in range(n):
            c, d = map(str,input().split())
            sala[c] = d

        for i in sala.keys():
            cont = 0
            for e in range(len(sala[i])):
                if sala[i][e] != orig[i][e]:
                    cont += 1
            if cont > 1:
                res += 1

        print(res)
    except EOFError:
        break